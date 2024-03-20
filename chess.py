#!/usr/bin/python3
"""This is the chess game screen module"""

import pygame
import sys

from const import *
from c_o_c import Chess
"""Imports the constants"""


class Game:
    """The class for the chess game screen"""
    def __init__(self):
        """Initialize the attributes"""
        pass

    def show_main_bg(self, surface):
        """Displays the background for the main menu"""
        bg_img = pygame.image.load('assets/title_screens/title_coc_2.png')
        scaled_bg = pygame.transform.scale(bg_img, (WIN_WIDTH, WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))

    def show_main_menu(self, surface):
        """Displays the main menu"""
        # Load the main menu
        main_menu = pygame.image.load('assets/menus/menu_list.png')
        main_menu.set_alpha(240)
        scaled_main_menu = pygame.transform.scale(main_menu, (WIN_WIDTH // 2.3, WIN_HEIGHT // 1.2))
        menu_x = (WIN_WIDTH - scaled_main_menu.get_width()) // 2
        menu_y = (WIN_HEIGHT - scaled_main_menu.get_height()) // 2
        # This is the underline for menu selection
        underline = pygame.image.load('assets/menus/underline.png')
        underline.set_alpha(0)
        underline_help = pygame.image.load('assets/menus/underline.png')
        underline_help.set_alpha(0)
        underline_exit = pygame.image.load('assets/menus/underline.png')
        underline_exit.set_alpha(0)
        underline_opt = pygame.image.load('assets/menus/underline.png')
        underline_opt.set_alpha(0)
        # Display text of main menu
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Play', True, (60, 60, 60), None)
        textRect = text.get_rect()
        textRect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2)

        menu_opt = font.render('Settings', True, (60, 60, 60), None)
        opt_rect = menu_opt.get_rect()
        opt_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50)

        menu_help = font.render('How To Play', True, (60, 60, 60), None)
        help_rect = menu_help.get_rect()
        help_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100)

        menu_exit = font.render('Exit', True, (60, 60, 60), None)
        exit_rect = menu_exit.get_rect()
        exit_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 150)

        play_line = text.get_rect()
        play_line.center = (WIN_WIDTH // 2 - 50, WIN_HEIGHT // 2 + 25)
        opt_line = menu_opt.get_rect()
        opt_line.center = (WIN_WIDTH // 2 - 15, WIN_HEIGHT // 2 + 75)
        help_line = menu_opt.get_rect()
        help_line.center = (WIN_WIDTH // 2 - 15, WIN_HEIGHT // 2 + 125)
        exit_line = menu_opt.get_rect()
        exit_line.center = (WIN_WIDTH // 2 - 15, WIN_HEIGHT // 2 + 175)

        surface.blit(scaled_main_menu, (menu_x, menu_y))
        # Draw the text
        surface.blit(text, textRect)
        surface.blit(menu_opt, opt_rect)
        surface.blit(menu_help, help_rect)
        surface.blit(menu_exit, exit_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    # Button clicked!
                    pygame.quit()
                    sys.exit()

                elif textRect.collidepoint(event.pos):
                    # Button clicked!
                    Chess.play_game()

                elif opt_rect.collidepoint(event.pos):
                    # Button clicked!
                    surface.fill((222, 222, 222))

                elif help_rect.collidepoint(event.pos):
                    # Button clicked!
                    surface.fill((222, 222, 222))

        # Check if the mouse is hovering over the text rectangle
        if textRect.collidepoint(pygame.mouse.get_pos()):
            # Make underline visible
            underline.set_alpha(255)
            surface.blit(underline, play_line)
        else:
            # Make underline invisible
            underline.set_alpha(0)
            surface.blit(underline, play_line)

        if opt_rect.collidepoint(pygame.mouse.get_pos()):
            underline_opt.set_alpha(255)
            surface.blit(underline_opt, opt_line)
        else:
            underline_opt.set_alpha(0)
            surface.blit(underline_opt, opt_line)

        if help_rect.collidepoint(pygame.mouse.get_pos()):
            underline_help.set_alpha(255)
            surface.blit(underline_help, help_line)
        else:
            underline_help.set_alpha(0)
            surface.blit(underline_help, help_line)

        if exit_rect.collidepoint(pygame.mouse.get_pos()):
            underline_exit.set_alpha(255)
            surface.blit(underline_exit, exit_line)
        else:
            underline_exit.set_alpha(0)
            surface.blit(underline_exit, exit_line)

    def show_game_bg(self, surface):
        """
        Displays the in-game background
        Loads the background image
        Resizes it then draws it on the screen
        """
        bg_img = pygame.image.load('assets/backgrounds/background_0.png')
        scaled_bg = pygame.transform.scale(bg_img, (WIN_WIDTH, WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))

    def show_cursor(self, surface):
        """Displays the custom cursor"""
        # Load custom mouse cursor
        cursor_image = pygame.image.load('assets\cursors\custom_cursor.png')
        # Hide default cursor
        pygame.mouse.set_visible(False)
        # Draw custom cursor
        cursor_rect = cursor_image.get_rect(center=pygame.mouse.get_pos())
        surface.blit(cursor_image, cursor_rect)

    def show_chessboard(self, surface):
        """Displays the chessboard"""
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (255, 255, 255) # White
                else:
                    color = (0, 0, 0) # Black

                rect = (col * SQUARE, row * SQUARE, SQUARE, SQUARE)
                pygame.draw.rect(surface, color, rect)

    def show_game_menu(self, surface):
        """Displays the menu"""
        game_menu = pygame.image.load('assets/menus/coc_menu.png')
        surface.blit(game_menu, (500, 200))