# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:56:48 2018

@author: adrie
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


fig = plt.figure(facecolor = 'k')

ax = plt.axes(xlim = (-3, 3), ylim = (-1.5, 1.5), facecolor = 'k')

line, = ax.plot([],[], 'w', lw = 2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(-np.pi*i, np.pi*i, 100)
    x1 = np.cos(x)
    x2 = np.sin(x)
    line.set_data(x1,x2)
    return line,


Ani = animation.FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit = True) 

#Ani.save('new_anitfton.mp4', fps=60)