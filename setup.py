#!/usr/bin/env python

from distutils.core import setup, Extension
from Cython.Build import cythonize

import numpy
include_dirs = [numpy.get_include(),]

ext_modules=[ Extension("contour",
                        ["contour.pyx", "conrec.cxx"],
                        include_dirs = [numpy.get_include(),]
                         )]

setup(
  name = 'contour',
  ext_modules = cythonize(ext_modules),
)

