# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:34:36 2018

@author: adrie
"""

from math import sin
from math import cos
import matplotlib.pyplot as plt


a = 0.4905


def f(u):
    return (u[1], a*sin(u[0]))


def Euler1(f, a, yo, zo, b, h):
    y = [yo,zo]
    t = a
    taby1 = [y[0]]
    taby2 = [y[1]]
    tabx = [t]
    while t < b:
        y = [y[0] + h*(f(y)[0]), y[1] + h*(f(y)[1])]
        taby1.append(y[0])
        taby2.append(y[1])
        t += h
        tabx.append(t)
    return taby1

def Euler2(f, a, yo, zo, b, h):
    y = [yo,zo]
    t = a
    taby1 = [y[0]]
    taby2 = [y[1]]
    tabx = [t]
    while t < b:
        y = [y[0] + h*(f(y)[0]), y[1] + h*(f(y)[1])]
        taby1.append(y[0])
        taby2.append(y[1])
        t += h
        tabx.append(t)
    return taby2

def Eulert(f, a, yo, zo, b, h):
    y = [yo,zo]
    t = a
    taby1 = [y[0]]
    taby2 = [y[1]]
    tabx = [t]
    while t < b:
        y = [y[0] + h*(f(y)[0]), y[1] + h*(f(y)[1])]
        taby1.append(y[0])
        taby2.append(y[1])
        t += h
        tabx.append(t)
    return tabx

#print(len(Euler1(f, 0., 0.5, 0., 16., 0.01)))

"""i = 0.
k = 0
p = 0.01
lx = [0.]
ly = [0.5]
while k < 1602:
    i += p
    k += 1
    lx.append(i)
    ly.append(0.5*cos(i))"""

plt.plot(Eulert(f, 0., 0.0872665, 0., 100., 0.001), Euler1(f, 0., 0.0872665, 0., 100., 0.001))
#plt.plot(lx,ly)

print("done")


#5.2