# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 22:38:55 2019

@author: adrie
"""

import matplotlib.pylab as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import cm


n = 10

fig1,ax1 = plt.subplots()
fig2,ax2 = plt.subplots()

ax1.set_title("Une incroyable image aléatoire")
ax2.set_title("Fabuleux, la même chose mais en noir et blanc. De plus, $e^{i\pi} = -1$")

im1 = ax1.imshow(np.random.rand(n,n), animated = True)
im2 = ax2.imshow(np.random.rand(n,n), animated = True, cmap = cm.gray)

cb1 = fig1.colorbar(im1)
cb2 = fig2.colorbar(im2)

def update1(x):
	im1.set_array(np.random.rand(n,n))
	ax1.set_title("Une incroyable image aléatoire, $n = $" + str(x))

def update2(x):
	im2.set_array(np.random.rand(n,n))
	return im2,

ani1 = FuncAnimation(fig1, update1, interval = 300)
ani2 = FuncAnimation(fig2, update2, interval = 300, blit = True)
