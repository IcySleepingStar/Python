# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:43:35 2018

@author: adrie
"""

import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
from math import pi
from math import cos
from math import sin




fig = plt.figure()
axe = plt.axes(xlim = (-1,1),ylim = (-1,1))


def update(x):
    plt.plot([cos(x)], [sin(x)], 'ko', )
    return 

def init():
    plt.plot([0],[0], 'ko')

l = []
i = 0
while i < (2*pi):
    l.append(i)
    i += 0.05



ani = FuncAnimation(fig, update, frames = l , interval = 0.01)