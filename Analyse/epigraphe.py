# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 23:29:11 2018

@author: adrie
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def f(x):
	return np.sin(x)

def epigraphe(f,xmin,xmax,ymin,ymax,nx,ny):
	lxs = []
	lys = []
	lxi = []
	lyi = []
	for x in np.linspace(xmin,xmax,nx):
		for y in np.linspace(ymin,ymax,ny):
			if f(x) < y:
				lxs.append(x)
				lys.append(y)
			else:
				lxi.append(x)
				lyi.append(y)
	plt.plot(lxs,lys, '.m', markersize = 50)
	plt.plot(lxi,lyi, color = (0.2,0.5,0.6,1), marker = '.',linestyle = 'none', markersize = 50)


epigraphe(f,-3,3,-1,1,50,50)