# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 00:33:14 2019

@author: adrie
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection = '3d')

theta = np.linspace(-10*np.pi, 10*np.pi, 1000)
z = np.linspace(-4, 4, 1000)
r = z**2 + 1

x = r * np.sin(theta)
y = r * np.cos(theta)

lx = [9, 5, 4, 4, 1, 2, 8, 4, 2]
ly = [2, 9, 4, 2, 4, 8, 1, 5, 4]
lz = [8, 4, 2, 5, 4, 2, 1, 4, 9]

ax.plot(x,y,z)