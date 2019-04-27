# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 09:43:37 2019

@author: adrie
"""

import pygame


pygame.init()
screen = pygame.display.set_mode((640,480))
font = pygame.font.SysFont('arial', 20)


class PygView:	 
    def run():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            text = "SECONDS"
            surface = font.render(text, True, (0, 255, 0))
            screen.blit(surface, (300, 200))
            pygame.display.flip()

        pygame.quit()

PygView.run()