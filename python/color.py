from __future__ import division
import matplotlib
matplotlib.use('Qt5Agg')
from pylab import imshow, show, get_cmap
from numpy import random

#Z = random.random((50,50))   # Test data
Z = []

for i in range(0,49):
    h = []
    for j in range (0, 49):
        h.append(j)
    Z.append(h)
imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
show()