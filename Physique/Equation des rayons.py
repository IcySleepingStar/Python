# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 20:31:28 2019

@author: adrie
"""

import numpy as np
import matplotlib.pylab as plt


# d/ds(n(m)u(M)) = grad(n(m))

# soit u(M + dM) = ((ds*grad(n(M))) + n(M)u(M))/(n(M + dM))

# avec gradf = df/dx*ex + df/dy*ey


# dimension

N = 1000

xmax = 1

dx = xmax/N


def f1(x,y):
	return 10*np.cos(10*x) + 10*np.sin(10*y)

def boule(x,y):
	if (x - 0.5)**2 + (y - 0.5)**2 < 0.2:
		return 2
	else:
		return 1
	
def boulegradext(x,y):
	if (x - 0.5)**2 + (y - 0.5)**2 < 0.2:
		return ((x - 0.5)**2 + (y - 0.5)**2)*10
	else:
		return 2
	
def boulegradint(x,y):
	if (x - 0.5)**2 + (y - 0.5)**2 < 0.2:
		return 5/(((x - 0.5)**2 + (y - 0.5)**2) + 0.1)
	else:
		return 16.5

def gridf(f):
	M = np.zeros((N,N))
	for i in range(N):
		for j in range(N):
			M[i,j] = f(i/N,j/N)
	return M


def lingrid(x,y):
	M = np.zeros((N,N))
	for i in range(N):
		M[i] = np.full(N,((y-x)*(i/N) + x))
	return M
	
#M = lingrid(1,100)

M = gridf(boulegradint)

plt.imshow(M, cmap = 'gray_r')

def grad(M,i,j):
	return np.array([(M[i, (j + 1)%N] - M[i,j])/dx, (M[(i + 1)%N, j] - M[i,j])/dx])

def rayon(x0,y0,u0,M,n,ds):
	lx = []
	ly = []
	x = x0
	y = y0
	u = u0
	for k in range(n):
		im = int((y/xmax)*N)%N
		jm = int((x/xmax)*N)%N
		x = x + u[0]*ds
		y = y + u[1]*ds
		imdm = int((y/xmax)*N)%N
		jmdm = int((x/xmax)*N)%N
		g = grad(M,im,jm)
		nm = M[im,jm]
		nmdm = M[imdm,jmdm]
		u = (1/nmdm)*(ds*g + nm*u)
		lx.append(N*x)
		ly.append(N*y)
	return lx,ly

lx,ly = rayon(0, 0.5, np.array([1,-1]), M, 20000, 0.0001)

plt.plot(lx,ly,'r')

lx2,ly2 = rayon(0, 0.5, np.array([1,-1.2]), M, 20000, 0.0001)

plt.plot(lx2,ly2,'g')

lx3,ly3 = rayon(0, 0.5, np.array([1,-1.4]), M, 20000, 0.0001)

plt.plot(lx3,ly3,'b')

plt.imshow(M, cmap = 'gray_r')
	
