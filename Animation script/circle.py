# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:57:53 2018

@author: adrie
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


fig = plt.figure(facecolor = 'k')

ax = plt.axes(xlim = (-3, 3), ylim = (-1.5, 1.5), facecolor = 'k')

line, = ax.plot([],[],lw = 2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.flip(np.linspace(-np.pi, np.pi, 100),0)
    x1 = np.cos(x)*i/100
    x2 = np.sin(x)*i/100
    line.set_data(x1,x2)
    return line,

Ani = animation.FuncAnimation(fig, animate, init_func = init, frames = 100, interval = 0.1, blit = True) 



