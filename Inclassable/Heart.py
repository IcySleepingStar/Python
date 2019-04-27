# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:31:44 2019

@author: adrie
"""

import numpy as np
import matplotlib.pylab as plt
from pylab import cm
n = 500

M = np.zeros((n,n))

def c(i):
	return (4*i)/n - 2

for i in range(n):
	for j in range(n):
		x = c(n - i)
		y = c(n - j)
		if x**2 + (y - abs(x)**0.5)**2 < 1:
			M[i,j] = 1

plt.imshow(M.T, cmap = cm.Spectral_r)