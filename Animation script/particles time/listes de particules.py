# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:14:11 2018

@author: adrie
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random

n = 1001
T = 10
h = T/n
a = 1
b = 0.1

class Particule:
	def __init__(self,x,y,vx,vy):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
	def position(self):
		return [self.x, self.y]
	def vitesse(self):
		return [self.vx, self.vy]
	def normev(self):
		return (self.vx**2 + self.vy**2)**(0.5)
	def bouger(self):
		self.x = self.x + (h * self.vx)
		self.y = self.y + (h * self.vy)

fig = plt.figure(facecolor = 'k')

ax = plt.axes(xlim = (-0.1, 1.1), ylim = (-0.1, 1.1), facecolor = 'k')

line, = ax.plot([],[], 'wo')


l = []
for i in range(50):
	x = Particule(random.random(),random.random(),random.random(),random.random())
	l.append(x)



def distance(p1,p2):
	[x1,y1] = p1.position()
	[x2,y2] = p2.position()
	return ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)


def collision(p1,p2):
	if distance(p1,p2) < b:
		[x1,y1] = p1.position()
		[x2,y2] = p2.position()
		vx,vy = (x2 - x1), (y2 - y1)
		v1,v2 = a*p1.normev(),a*p2.normev()
		alpha = np.arccos(vx/((vx**2 + vy**2)**(0.5)))
		p1.vx = - v1*np.cos(alpha)
		p2.vx = v2*np.cos(alpha)
		p1.vy = - v1*np.sin(alpha)
		p2.vy = v2*np.sin(alpha)
		
def mur(p):
	[x,y] = p.position()
	if x > 1 or x < 0:
		p.vx = -p.vx
	if y > 1 or y < 0:
		p.vy = -p.vy

# maintenant avec des listes de particules

def newstep(l):
	n = len(l)
	i = 0
	while i < n:
		j = 0
		while j < n:
			if j != i:
				collision(l[i],l[j])
			j += 1
		i += 1
	i = 0
	while i < n:
		mur(l[i])
		l[i].bouger()
		i += 1


def animate(i):
	newstep(l)
	n = len(l)
	line.set_data([l[i].x for i in range(n)],[l[i].y for i in range(n)])
	return line,

	
	
Ani = animation.FuncAnimation(fig, animate, frames = 20000, interval = 1, blit = True)

Ani.save('splendide_particules++.mp4', fps=60)

 