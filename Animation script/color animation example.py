# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 23:38:10 2018

@author: adrie
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(1,1)
ax.set(xlim=(-3, 3), ylim=(-3, 3))

"""
x = np.linspace(-3, 3, 91)
t = np.linspace(1, 25, 30)
X2, T2 = np.meshgrid(x, t)
 
sinT2 = np.sin(2*np.pi*T2/T2.max())
F = 0.9*sinT2*np.sinc(X2*(1 + sinT2))

line = ax.plot(x, F[0, :], color='k', lw=2)[0]

def animate(i):
    line.set_ydata(F[i, :])
"""


x = np.linspace(-3, 3, 91)
t = np.linspace(0, 25, 30)
y = np.linspace(-3, 3, 91)
X3, Y3, T3 = np.meshgrid(x, y, t)
sinT3 = np.sin(2*np.pi*T3 /
               T3.max(axis=2)[:,:,np.newaxis])
G = (X3**2 + Y3**2)*sinT3


cax = ax.pcolormesh(x, y, G[:-1, :-1, 0],
                    vmin=-1, vmax=1, cmap='Blues')
fig.colorbar(cax)

def animate(i):
     cax.set_array(G[:-1, :-1, i].flatten())


 
plt.draw()
plt.show()

anim = FuncAnimation(
    fig, animate, interval=100, frames=len(t)-1)