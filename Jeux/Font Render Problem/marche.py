# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:15:23 2019

@author: adrie
"""

import pygame

class PygView(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        self.font = pygame.font.SysFont('arial', 20)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            text = "SECONDS"
            surface = self.font.render(text, True, (0, 255, 0))
            self.screen.blit(surface, (300, 200))
            pygame.display.flip()

        pygame.quit()

PygView().run()