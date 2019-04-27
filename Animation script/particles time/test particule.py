# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:01:14 2018

@author: adrie
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as anim

n = 398
T = 10
h = T/n

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
	if distance(p1,p2) < 0.1:
		[x1,y1] = p1.position()
		[x2,y2] = p2.position()
		vx,vy = (x1 - x2), (y1 - y2)
		p1.vx = vx
		p2.vx = - vx
		p1.vx = vy
		p2.vy = - vy


def newstep(p1,p2):
	collision(p1,p2)
	p1.bouger()
	p2.bouger()


p1 = Particule(1,0,-1,0)
p2 = Particule(-1,0,1,0)

dot1, = ax.plot([],[],'ko')

dot2, = ax.plot([],[],'ro')


def animate(i):
	newstep(p1,p2)
	plt.plot([p1.x, p2.x], [p1.y, p2.y],'.')
	
def animate2(i):
	newstep(p1,p2)
	dot1.set_data([p2.x], [p2.y])
	dot2.set_data([p1.x], [p1.y])


Ani = anim.FuncAnimation(fig, animate2, frames = 10, interval = 0.01,blit = False) 

	

