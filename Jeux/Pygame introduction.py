# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:03:43 2019

@author: adrie
"""

import pygame

def find1(l):
	for k in range(len(l)):
		if l[k] == 1:
			print(k)
			print("\n")

pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()

sound = pygame.mixer.Sound('Sound Effects//Explosion_Ultra_Bass-Mark_DiAngelo-1810420658.wav')

screen = pygame.display.set_mode((640,480))

background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background.convert()
screen.blit(background,(0,0))

ball = pygame.Surface((20,20))
ball.fill((255,255,255))
pygame.draw.circle(ball,(0,0,0),(10,10),10)
ball.convert()

clock = pygame.time.Clock()

playtime = 0

mainloop = True

x,y = 320,240

while mainloop:
	
	ms = clock.tick(30)
	playtime += ms/1000
	
	screen.blit(background,(0,0))
	screen.blit(ball,(x,y))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			mainloop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				mainloop = False
			if event.key == pygame.K_SPACE:
				print("EXPLOSION")
				sound.play(maxtime = 2000,fade_ms = 1000)
			if event.key == pygame.K_RIGHT:
				x += 20
				sound.play(maxtime = 2000)
			if event.key == pygame.K_LEFT:
				x -= 20
			if event.key == pygame.K_UP:
				y -= 20
			if event.key == pygame.K_DOWN:
				y += 20
			
	
	title = "you have played " + str(int(playtime*100)/100) + " seconds"
	pygame.display.set_caption(title)
	
	
	pygame.display.flip()

pygame.quit()

