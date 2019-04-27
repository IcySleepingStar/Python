# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:19:11 2018

@author: adrie
"""

import matplotlib.pylab as plt
import numpy as np

n = 101

l = [i - n//2 for i in range(n)]

lx = []
for i in l:
	lx = lx + n*[i]

ly = n*l

"""
plt.plot(lx,ly,'.k')

for i in range(n):
	plt.plot(lx[n*i:(n*i + n)], ly[n*i:(n*i + n)], '--k')
"""


def transformation(f,lx,ly):
	n = len(lx)
	k = 0
	nlx = []
	nly = []
	while k < n:
		(ni,nj) = f(lx[k], ly[k])
		nlx.append(ni)
		nly.append(nj)
		k += 1
	return (nlx,nly)



def homotethie(i,j):
	return (2*i,2*j)


def somme(i,j):
	return (i + j, j)

theta = np.pi/12

def rotation(i,j):
	return (np.cos(theta)*i + np.sin(theta)*j, - np.cos(theta)*j + np.sin(theta)*i)

def truc(i,j):
	mod = (i**2) + (j**2)
	if mod == 0:
		return (0,0)
	else:
		return ((i/mod), - j/mod)


(nlx,nly) = transformation(truc, lx, ly)

plt.plot(nlx,nly,'.b')



for i in range(n):
	plt.plot(nlx[n*i:(n*i + n)], nly[n*i:(n*i + n)], '--b')












plt.axis('scaled')