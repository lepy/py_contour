#!/usr/bin/env python

# simple test code for contour

import numpy as np
import py_contour
# import py_gd # so we can see the results visually

M, N = 1000, 800 #(image size)
# create an array:

x = np.linspace(0, 3*np.pi, 40)
y = np.linspace(0, 3*np.pi, 32) * 0.8
# reshape x:
x.shape = (-1, 1)
z = np.cos(x) + np.sin(y)


levels = np.linspace(z.min(),z.max(), 12)
levels = levels[1:-1]
print levels
segs = py_contour.contour( z,
                        x,
                        y,
                        levels,
                       )

scale_factor = np.array((M / (x.max() - x.min()), N / (y.max() - y.min()) ))
shift = np.array ( (x.min(), y.min()) )

def scale( points ):
    return np.asarray(points)*scale_factor + shift

# scale the values:
for level in segs:
    segs[level] = scale(segs[level])


for level, segments in segs.items():
    print "level:", level

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# sort the segments ....
polygons = {}
for level, segments in segs.items():
    print "level", level
    polygons[level] = py_contour.sort_segments(segments)

print polygons

#plotting
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')

for level, polys in polygons.items():
    print "level", level
    for p in polys:
        df = pd.DataFrame(p, columns=["x", "y"])
        df["z"] = level
        print df.head()
        plt.plot(df.x, df.y, df.z)

plt.show()
