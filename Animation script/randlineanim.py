# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:54:31 2018

@author: adrie
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random as rand



fig = plt.figure(facecolor = 'k')
ax = plt.axes(xlim = (0,4), ylim = (0,2), facecolor = 'k')
line, = ax.plot([],[],linestyle = '-', color = 'w', lw = 4)



def init():
    line.set_data([], [])
    return line,


def animate(i):
    l = []
    ll = []
    for k in range (1):
        l.append(rand.random()*4)
        ll.append(rand.random()*2)
    ll.append(ll[0])
    l.append(rand.random()*4)
    line.set_data(l,ll)
    return line,


Ani = animation.FuncAnimation(fig, animate, init_func = init, frames = 2000, interval = 2, blit = True) 