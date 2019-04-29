# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:30:57 2019

@author: adrie
"""

import matplotlib.pylab as plt
import numpy as np

#delta
d = 4

#length of the time step
dt = 0.01

#time of the simulation
T = 3

#number of steps
n = int(T/dt)

#list of x (we compute solution for x > 0)
lx = np.linspace(0,T,n)

#list of f(x)
f1x = np.full((n),1.)

#current value of f
f1 = 1
#current value of f'
f2 = -d



for k in range(1,n):
	f1x[k] = f1
	x = k*dt
	f2 += dt*(((x - 1)*f2 - d*f1)/x)
	f1 += dt*f2

plt.plot(lx,f1x)


#here we compute the power series up to the 10th term

lp = [1,-d]

for k in range(1,10):
	lp.append((k - d)*lp[-1]/(k + 1)**2)

#here we compute p(x) for the same x as f

px = []

for k in lx:
	s = 0
	for i in range(len(lp)):
		s += (lp[i])*(k**i)
	px.append(s)

plt.plot(lx,px)