# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:06:24 2019

@author: adrie
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    font = pygame.font.SysFont('arial', 20)
    text = "SECONDS"
    surface = font.render(text, True, (0, 255, 0))
    screen.blit(surface, (300, 200))
    pygame.display.flip()
    del(font)    
	 
	
pygame.quit()