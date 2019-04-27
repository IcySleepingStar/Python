# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:44:27 2019

@author: adrie
"""

import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure(facecolor = 'k')
ax = plt.axes(facecolor = 'k')


def DistanceEuclidienne(A,B):
	xa,ya = A
	xb,yb = B
	return (((xa - xb)**2) + ((ya - yb)**2))**0.5


def FindC(A,B):
	xa,ya = A
	xb,yb = B
	xc = xa + (xb - xa)/2 - (yb - ya)/2
	yc = ya + (xb - xa)/2 + (yb - ya)/2
	return xc,yc


def Plotable(l):
	lx,ly = [],[]
	for M in l:
		x,y = M
		lx.append(x)
		ly.append(y)
	return lx,ly

def Plot(l):
	lx,ly = Plotable(l)
	plt.plot(lx,ly)


def dragon(n,A,B):
	if n == 1:
		return [A,B]
	else:
		C = FindC(A,B)
		d1 = dragon(n - 1, A, C)
		d2 = dragon(n - 1, B, C)
		d2.pop()
		d2.reverse()
		return d1 + d2

wyvern = dragon(18,(0,0),(1,1))

#Plot(wyvern)

k = 100

n = int((len(wyvern) - 1)/k)

#plt.axis('scaled')

jormungandr = Plotable(wyvern)
jorx,jory = jormungandr

def fastupdate(i):
	lx = jorx[i*k:i*k + k]
	ly = jory[i*k:i*k + k]
	plt.plot(lx,ly,'w')

def update(i):
	x1,y1 = wyvern[i]
	x2,y2 = wyvern[i + 1]
	plt.plot([x1,x2],[y1,y2])

anim = FuncAnimation(fig, fastupdate, interval = 10, frames = n)

anim.save('DragonFlight8.mp4',dpi = 250)