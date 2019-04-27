# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:36:32 2018

@author: adrie
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random

n = 3

fig = plt.figure()

ax = plt.axes(xlim = (-1, 1), ylim = (-1, 1))

plt.axis('equal')

def norme(n,m):
	for i in range(m):
		x,y = 1 - 2*random.random(),1 - 2*random.random()
		if ((abs(x)**n) + (abs(y)**n))**(1/n) < 1:
			plt.plot([x],[y],'k.')
		

norme(n,10000)
