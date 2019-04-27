# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:15:22 2019

@author: adrie
"""


import numpy as np
import matplotlib.pylab as plt
from pylab import cm
from matplotlib.animation import FuncAnimation
import random
import copy

# probabilité d'aller à gauche

g = 0.2

# probabilité d'aller à droite

d = 0.2

# probabilité d'aller en haut

h = 0.2

# probabilité d'aller en bas

b = 0.2

# probabilité de rester en place

s = 1 - g - d - h - b

# la taille de l'espace

n = 100

# nombre de particule

N = 1000

# la grille

G = np.zeros((2*n + 1, 2*n + 1))

G[n][n] = N

beurk = [G]

	

fig,ax = plt.subplots()

space = ax.pcolormesh(beurk[0][:-1,:-1], vmin = 0, vmax = 1, cmap = cm.gray)
comap = fig.colorbar(space)

def reduire(P):
	maxi = 0
	mini = N
	a,b = np.shape(P)
	M = np.zeros((a,b))
	for i in range(a):
		for j in range(b):			
			if P[i][j] > maxi:
				maxi = P[i][j]
			if P[i][j] < mini:
				mini = P[i][j]
	for i in range(a):
		for j in range(b):
			M[i][j] = (P[i][j] - mini)/(maxi - mini)
	return M
			

def step(m):
	nG = np.zeros((2*n + 1, 2*n + 1))
	for i in range(2*n + 1):
		for j in range(2*n + 1):
			x = int(beurk[0][i][j])
			for a in range(x):
				r = random.random()
				if r <= g:
					nG[i][(j - 1) % (2*n + 1)] += 1
				if g < r <= g + d:
					nG[i][(j + 1) % (2*n + 1)] += 1
				if g + d < r <= g + d + b:
					nG[(i - 1) % (2*n + 1)][j] += 1
				if g + d + b < r <= g + d + b + h:
					nG[(i + 1) % (2*n + 1)][j] += 1
				if 1 - s < r:
					nG[i][j] += 1
	beurk[0] = nG
	M = copy.copy(beurk[0])
	P = reduire(M)
	space.set_array(P[:-1,:-1].flatten())
	
anim = FuncAnimation(fig, step, interval = 10, frames = 10000)

#anim.save('SuperMarch.mp4',dpi = 250)