# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:56:40 2018

@author: adrie
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


fig = plt.figure()

ax = plt.axes(xlim = (-1.5, 1.5), ylim = (-1.5, 1.5))

line, = ax.plot([],[],lw = 2)

def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = np.linspace(-np.pi*i, np.pi*i, 100)
    x1 = np.cos(x)
    x2 = np.sin(x)
    line.set_data(x1,x2)
    return line,

Ani = animation.FuncAnimation(fig, animate, init_func = init, frames = 2000, interval = 20, blit = True) 