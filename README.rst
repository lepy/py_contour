#py_contour

Computing contour polygons from data on a rectangular grid.

Cython wrappers around a C library contouring code found here:

http://paulbourke.net/papers/conrec/

Generates contour lines and polygons from recatagular grid of data.

Note that the C lib generates only line segments, which is great for drawing contour lines, but if you need to fill polygons, the code also sorts the line segments into polygons and polylines (for non-closed contours)

## Installation

### Dependencies

Run Time:

* numpy

Built Time:

* setuptools'
* numpy
* cython>0.23
* pytest

### Building

I don't currently have binary wheels available, so you need to have a properly configured C complier, etc.

Otherwise, download the source code from gitHub, either as a clone or source tarball::

    pip install ./

should do it. or::

    pip install -e ./

For "editable mode"

Regular old::

    setup.py install

Should work too, but then you get that easy-install garbage scattered around.

### Testing

You should be able to run the tests from source with::

  python setup.py test

Or run the installed tests with::

  py.test --pyargs py_contour 

### demo

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





