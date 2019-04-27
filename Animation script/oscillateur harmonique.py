# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:40:42 2018

@author: adrie
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


omega2 = 10

#  y'' + omega2*sin(y) = 0


def createtab(x0, xx0):
    h = 1/1000
    tabx1 = [x0]
    tabx2 = [xx0]
    tabx3 = []
    i = 1
    while i < 20001:
        tabx3.append(- omega2*np.sin(tabx1[i - 1]))
        tabx2.append(tabx2[i - 1] + (h*tabx3[i - 1]))
        tabx1.append(tabx1[i - 1] + (h*tabx2[i - 1]))
        i += 1
    return tabx1

l = createtab(2, 0)
#print(l)




fig = plt.figure()
ax = plt.axes(xlim = (-4,4), ylim = (-2,2))
line, = ax.plot([],[],'b.', linestyle = '-', color = 'k', lw = 2)



def init():
    line.set_data([], [])
    return line,


def animate(i):
    line.set_data([0,l[10*i]],[0,0])
    return line,


Ani = animation.FuncAnimation(fig, animate, init_func = init, frames = 2000, interval = 10, blit = True) 