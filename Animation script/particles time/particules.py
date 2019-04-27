# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:06:26 2018

@author: adrie
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

n = 1001
T = 10
h = T/n
a = 1
b = 0.3

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

fig = plt.figure()

ax = plt.axes(xlim = (-3, 3), ylim = (-1.5, 1.5))



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
		

def newstep(p1,p2):
	collision(p1,p2)
	p1.bouger()
	p2.bouger()


p1 = Particule(0,1,0,-1)
p2 = Particule(1,0,-1,0)

dot1, = ax.plot([],[],'bo')

dot2, = ax.plot([],[],'ro')


def animate(i):
	newstep(p1,p2)
	dot1.set_data([p1.x], [p1.y])
	dot2.set_data([p2.x], [p2.y])

Ani = animation.FuncAnimation(fig, animate, frames = 200, interval = 100, blit = False) 


		




