# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 12:19:33 2019

@author: adrie
"""

import numpy as np
import matplotlib.pylab as plt
from pylab import cm
from matplotlib.animation import FuncAnimation
import random
import copy

# probabilité d'aller à gauche

g = 0.3

# probabilité d'aller à droite

d = 0.3

# probabilité de rester à sa place

s = 1 - d - g

# la taille de l'espace

n = 100

# la grille

xl = np.zeros((100,2*n + 1))

beurk = [xl]

# nombre de particule

N = 1000

for i in range(100):
	beurk[0][i][n] = N
	
	
fig,ax = plt.subplots()

space = ax.pcolormesh(beurk[0][:-1,:-1], vmin = 0, vmax = 1, cmap = cm.gray)
comap = fig.colorbar(space)

def reduire(P):
	maxi = 0
	mini = N
	for k in range(2*n + 1):
		if P[0][k] > maxi:
			maxi = P[0][k]
		if P[0][k] < mini:
			mini = P[0][k]
	for k in range(2*n + 1):
		for i in range(100):
			P[i][k] = (P[i][k] - mini)/(maxi - mini)
	return P
			

def step(m):
	nxl = np.zeros((100,2*n + 1))
	for k in range(2*n + 1):
		x = int(beurk[0][0][k])
		for a in range(x):
			r = random.random()
			if r < g:
				for i in range(100):	
					nxl[i][k - 1] += 1
			else:
				if r > (1 - d):
					for i in range(100):	
						nxl[i][k + 1] += 1
				else:
					for i in range(100):	
						nxl[i][k] += 1
	beurk[0] = nxl
	M = copy.copy(beurk[0])
	P = reduire(M)
	space.set_array(P[:-1,:-1].flatten())
	
anim = FuncAnimation(fig, step, interval = 50, frames = 300)

#anim.save('test.mp4',dpi = 250)