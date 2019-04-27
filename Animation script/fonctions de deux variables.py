# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:13:24 2018

@author: adrie
"""

import matplotlib.pylab as plt
import numpy as np
from pylab import cm
from matplotlib.animation import FuncAnimation

fig,axes = plt.subplots()

x = np.linspace(-4,4,70)
y = np.linspace(-4,4,70)
t = np.linspace(0,10,100)

X,Y,T = np.meshgrid(x,y,t)

Z = ((Y*T)**2)/(X**2 + Y**2 + np.exp(T))

graph = axes.pcolormesh(x,y,Z[:-1,:-1,0],cmap = cm.inferno)
axes.set_title('t = ?')

fig.colorbar(graph)

#g2 = plt.imshow(Z.T, extent=[-4, 4, -4, 4])

#g2.set_interpolation('bilinear')

#cnt = plt.contour(Z.T,extent=[-4, 4, -4, 4])


def update(n):
	graph.set_array(Z[:-1,:-1,n].flatten())
	axes.set_title('t='+str(n/10)+'s')

anim = FuncAnimation(fig, update, interval=100, frames=len(t)-1)