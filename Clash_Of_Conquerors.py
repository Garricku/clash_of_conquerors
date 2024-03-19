#!/usr/bin/python3
"""Clash of Conquerors - Chess Game"""

import pygame
import sys
"""These are imported modules used for game creation"""


# Window size
win_width = 1280
win_height = 720

# Load custom mouse cursor
cursor_image = pygame.image.load('assets/cursors/custom_cursor.png')

# Load background image
background_image = pygame.image.load('assets/title_screens/title_coc_2.png')
scaled_background = pygame.transform.scale(background_image, (win_width, win_height))

# Load the main menu
main_menu = pygame.image.load('assets/menus/menu_list.png')
main_menu.set_alpha(240)
scaled_main_menu = pygame.transform.scale(main_menu, (win_width // 2, win_height // 1.2))
menu_x = (win_width - scaled_main_menu.get_width()) // 2
menu_y = (win_height - scaled_main_menu.get_height()) // 2

# Load and set the icon
icon_image = pygame.image.load('assets/icons/coc_icon_bigger.png')
pygame.display.set_icon(icon_image)

# This is the underline for menu selection
underline = pygame.image.load('assets/menus/underline.png')
underline.set_alpha(0)
underline_help = pygame.image.load('assets/menus/underline.png')
underline_help.set_alpha(0)
underline_exit = pygame.image.load('assets/menus/underline.png')
underline_exit.set_alpha(0)
underline_opt = pygame.image.load('assets/menus/underline.png')
underline_opt.set_alpha(0)

pygame.init()

# Set game window
screen = pygame.display.set_mode((win_width, win_height), pygame.FULLSCREEN)
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

play_line = text.get_rect()
play_line.center = (win_width // 2 - 50, win_height // 2 + 25)
opt_line = menu_opt.get_rect()
opt_line.center = (win_width // 2 - 15, win_height // 2 + 75)
help_line = menu_opt.get_rect()
help_line.center = (win_width // 2 - 15, win_height // 2 + 125)
exit_line = menu_opt.get_rect()
exit_line.center = (win_width // 2 - 15, win_height // 2 + 175)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rect.collidepoint(event.pos):
                # Button clicked!
                pygame.quit()
                sys.exit()

            elif textRect.collidepoint(event.pos):
                # Button clicked!
                screen.fill((0, 0, 0))

            elif opt_rect.collidepoint(event.pos):
                # Button clicked!
                screen.fill((0, 0, 0))

            elif help_rect.collidepoint(event.pos):
                # Button clicked!
                screen.fill((0, 0, 0))

    # Check if the mouse is hovering over the text rectangle
    if textRect.collidepoint(pygame.mouse.get_pos()):
        # Make underline visible
        underline.set_alpha(255)
    else:
        # Make underline invisible
        underline.set_alpha(0)

    if opt_rect.collidepoint(pygame.mouse.get_pos()):
        underline_opt.set_alpha(255)
    else:
        underline_opt.set_alpha(0)

    if help_rect.collidepoint(pygame.mouse.get_pos()):
        underline_help.set_alpha(255)
    else:
        underline_help.set_alpha(0)

    if exit_rect.collidepoint(pygame.mouse.get_pos()):
        underline_exit.set_alpha(255)
    else:
        underline_exit.set_alpha(0)

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
    screen.blit(underline, play_line)
    screen.blit(underline_help, help_line)
    screen.blit(underline_opt, opt_line)
    screen.blit(underline_exit, exit_line)

    # Draw custom cursor
    cursor_rect = cursor_image.get_rect(center=pygame.mouse.get_pos())
    screen.blit(cursor_image, cursor_rect)

    # Keep display updated
    pygame.display.update()
