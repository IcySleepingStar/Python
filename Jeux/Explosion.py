# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:01:36 2019

@author: adrie
"""

import pygame
import random as rd

xsize = 1920
ysize = 1080

#xsize = 640
#ysize = 480

v = 0.5


pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()

pygame.mixer.music.load('Music//Cool and Good.ogg')
exp1 = pygame.mixer.Sound('Sound Effects//Shotgun_blast.wav')
exp2 = pygame.mixer.Sound('Sound Effects//Bomb_Exploding.wav')
exp3 = pygame.mixer.Sound('Sound Effects//Sonic Boom.wav')
exp4 = pygame.mixer.Sound('Sound Effects//Blast.wav')

pygame.mixer.music.play(-1)

exp_sound = False

screen = pygame.display.set_mode((xsize,ysize),pygame.FULLSCREEN)

background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background.convert()
screen.blit(background,(0,0))

ball = pygame.Surface((20,20))
ball.fill((255,255,255))
ball.set_colorkey((255,255,255))
pygame.draw.circle(ball,(0,0,0),(10,10),10)
ball.convert()

class explosion:
	def __init__(self,xmax,ymax):
		self.x = rd.randint(0,xmax - 1)
		self.y = rd.randint(0,ymax - 1)
		self.r = 0
		self.speed = 0.3
		self.color = (rd.random()*255,rd.random()*255,rd.random()*255)
	def expand(self,ms):
		if self.speed > 0 and rd.random() < 0.03:
			self.speed = -self.speed
		self.r += ms*self.speed
	def paint(self):
		pygame.draw.circle(screen,self.color,(self.x,self.y),int(self.r))

class boom:
	def __init__(self,emax,p,xmax,ymax):
		self.list = []
		self.emax = emax
		self.p = p
		self.xmax = xmax
		self.ymax = ymax
	def new_explosion(self):
		if len(self.list) < self.emax:
			if rd.random() < self.p:
				e = explosion(self.xmax, self.ymax)
				self.list.append(e)
				if exp_sound:
					pr = rd.random()
					if pr < 0.25:
						exp1.play()
					elif pr < 0.5:
						exp2.play()
					elif pr < 0.75:
						exp3.play()
					else:
						exp4.play()
	def expand_boom(self,ms):
		for e in self.list:
			e.expand(ms)
	def paint_boom(self):
		for e in self.list:
			if e.r < 0:
				self.list.remove(e)
			else:
				e.paint()
	def run(self,ms):
		self.new_explosion()
		self.expand_boom(ms)
		self.paint_boom()
	def intersect(self,x,y):
		for e in self.list:
			if (x - e.x)**2 + (y - e.y)**2 < e.r**2:
				return True
		return False
			
b = boom(3,0.05,xsize,ysize)

clock = pygame.time.Clock()

playtime = 0

mainloop = True

x,y = rd.randint(0,xsize - 1),rd.randint(0,ysize - 1)
dx,dy = 0,0

while mainloop:
	
	ms = clock.tick(30)
	playtime += ms/1000

	l = pygame.key.get_pressed()
	
	if l[275] == 1:
		dx = v
	elif l[276] == 1:
		dx = -v
	else:
		dx = 0
	
	if l[274] == 1:
		dy = v
	elif l[273] == 1:
		dy = -v
	else:
		dy = 0
	
	x = (x + dx*ms) % xsize
	y = (y + dy*ms) % ysize
	
	
	screen.blit(background,(0,0))
	
	b.run(ms)	
	
	font = pygame.font.SysFont('mono', 20, bold = True)
	
	text = "You have survived " + str(int(playtime*100)/100) + " seconds"
	textsurface = font.render(text,True,(0,0,0))
	screen.blit(textsurface,(20,20))
	
	command = "Press SPACE to mute/unmute the explosions"
	commandsurface = font.render(command,True,(0,0,0))
	cx,cy = font.size(command)
	screen.blit(commandsurface,(xsize - cx - 20, 20))
	
	
	screen.blit(ball,(x,y))
	
	if b.intersect(x,y):
		mainloop = False
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			mainloop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				mainloop = False
			if event.key == pygame.K_SPACE:
				if exp_sound:
					exp_sound = False
				else:
					exp_sound = True

	title = "SUPER GAME"
	pygame.display.set_caption(title)
	
	pygame.display.flip()
	
	del(font)

pygame.quit()

print("Congratulation ! You have survived " + str(int(playtime*100)/100) + " seconds")