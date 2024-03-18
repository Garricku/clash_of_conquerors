#!/usr/bin/python3
"""Clash of Conquerors - Chess Game"""

import pygame
import sys
"""These are imported modules used for game creation"""


# Initialize Pygame
pygame.init()

# Load title screen
bg_img = pygame.image.load('assets/title_screens/title_coc_2')

# Set game window
win_width = background_image.get_width()
win_height = background_image.get_height()
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Clash Of Conquerors")

# Load the custom mouse cursor
cursor_img = pygame.image.load("assets/cursors/custom_cursor")
pygame.mouse.set_visible(False) # Hides the default cursor

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Display the background image
    screen.blit(bg_img, (0, 0))

    # Display the custom cursor
    cursor_rect = cursor_img.get_rect(center=pygame.mouse.get_pos())
    screen.blit(cursor_img, cursor_rect)

    pygame.display.flip()
    clock.tick(60) # Frame rate limit

pygame.quit()
sys.exit()
