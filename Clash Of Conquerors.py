#!/usr/bin/python3
"""Clash of Conquerors - Chess Game"""

import pygame
import sys
"""These are imported modules used for game creation"""


# Window size
win_width = 1024
win_height = 600

# Load custom mouse cursor
cursor_image = pygame.image.load('assets\cursors\custom_cursor.png')

# Load background image
background_image = pygame.image.load('assets/title_screens/title_coc_2.png')
scaled_background = pygame.transform.scale(background_image, (win_width, win_height))
scaled_cursor_image = pygame.transform.scale(cursor_image, (50, 50))

# Load the main menu
main_menu = pygame.image.load('assets/menus/menu_list.png')
main_menu.set_alpha(240)
scaled_main_menu = pygame.transform.scale(main_menu, (win_width // 2, win_height // 1.2))
menu_x = (win_width - scaled_main_menu.get_width()) // 2
menu_y = (win_height - scaled_main_menu.get_height()) // 2

# Load and set the icon
icon_image = pygame.image.load('assets/icons/coc_icon_bigger.png')
pygame.display.set_icon(icon_image)


pygame.init()

# Set game window
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Clash Of Conquerors")
pygame.mouse.set_visible(False)  # Hide default cursor

# Display text of main menu
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Play', True, (60, 60, 60), None)
textRect = text.get_rect()
textRect.center = (win_width // 2, win_height // 2)

menu_opt = font.render('Settings', True, (60, 60, 60), None)
opt_rect = menu_opt.get_rect()
opt_rect.center = (win_width // 2, win_height // 2 + 50)

menu_help = font.render('How To Play', True, (60, 60, 60), None)
help_rect = menu_help.get_rect()
help_rect.center = (win_width // 2, win_height // 2 + 100)

menu_exit = font.render('Exit', True, (60, 60, 60), None)
exit_rect = menu_exit.get_rect()
exit_rect.center = (win_width // 2, win_height // 2 + 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw background image
    screen.blit(scaled_background, (0, 0))

    # Draw main menu
    main_menu = pygame.image.load('assets/menus/menu_list.png').convert_alpha()
    screen.blit(scaled_main_menu, (menu_x, menu_y))

    # Draw the text
    screen.blit(text, textRect)
    screen.blit(menu_opt, opt_rect)
    screen.blit(menu_help, help_rect)
    screen.blit(menu_exit, exit_rect)

    # Draw custom cursor
    cursor_rect = cursor_image.get_rect(center=pygame.mouse.get_pos())
    screen.blit(scaled_cursor_image, cursor_rect)

    # Keep display updated
    pygame.display.update()