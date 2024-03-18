#!/usr/bin/python3
"""Clash of Conquerors - Chess Game"""

import pygame
import sys
"""These are imported modules used for game creation"""


win_width = 1920
win_height = 1080

class Main:
    """This is the games main operations"""
    def __init__(self):
        """Initialize the Pygame"""
        pygame.init()
        
        # Set game window
        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Clash Of Conquerors")

    def main_loop(self):
        """This is the main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Keep display updated
        pygame.display.update()

main = Main()
main.main_loop()
