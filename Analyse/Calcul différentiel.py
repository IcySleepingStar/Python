# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 23:39:27 2019

@author: adrie
"""

import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm

figure,ax = plt.subplots()

x = np.linspace(-5,5,100)

X,Y = np.meshgrid(x,x)

Z = np.log(X**2 + Y**2)

im = ax.imshow(Z, cmap = cm.magma, interpolation = 'bilinear')
ax.set_title(r"$Une$ $fonction$ $harmonique:$ $f(x,y) = ln(x^2 + y^2)$")
cb = figure.colorbar(im)



fig2,ax2 = plt.subplots()

x2 = np.linspace(-10,10,100)
y2 = np.linspace(-1,1,100)

X2,Y2 = np.meshgrid(x2,y2)

Z2 = np.sin(X2) * np.exp(Y2)

im2 = ax2.imshow(Z2, cmap = cm.magma, interpolation = 'bilinear')
ax2.set_title(r"$Une$ $autre$ $fonction$ $harmonique:$ $f(x,y) = sin(x)e^y$")
cb2 = fig2.colorbar(im2)