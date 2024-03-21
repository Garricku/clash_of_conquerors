#!/usr/bin/python3
"""This is the chess game screen module"""

import pygame
import sys

from const import *
"""Imports the constants"""


class Game:
    """The class for the chess game screen"""
    def __init__(self):
        """Initialize the attributes"""
        self.play = False
        self.opt = False
        self.help = False
        self.menu_state = False

    def get_play(self):
        """Returns the play attribute bool"""
        return self.play

    def get_opt(self):
        """Returns the opt attribute bool"""
        return self.opt

    def get_help(self):
        """Returns the help attribute bool"""
        return self.help

    def get_menu_state(self):
        """Returns the state of game menu"""
        return self.menu_state

    def set_play(self, state):
        """Sets the play attribute bool"""
        self.play = state

    def set_opt(self, state):
        """Sets the opt attribute bool"""
        self.opt = state

    def set_help(self, state):
        """Sets the help attribute bool"""
        self.help = state

    def set_menu_state(self, state):
        """Sets the state of the in game menu"""
        self.menu_state = state

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
                    self.set_play(True)

                elif opt_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_opt(True)

                elif help_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_help(True)

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

    def show_cursor(self, surface):
        """Displays the custom cursor"""
        # Load custom mouse cursor
        cursor_image = pygame.image.load('assets\cursors\custom_cursor.png')
        # Hide default cursor
        pygame.mouse.set_visible(False)
        # Draw custom cursor
        cursor_rect = cursor_image.get_rect(center=pygame.mouse.get_pos())
        surface.blit(cursor_image, cursor_rect)

    def show_game_bg(self, surface):
        """
        Displays the in-game background
        Loads the background image
        Resizes it then draws it on the screen
        """
        bg_img = pygame.image.load('assets/backgrounds/background_0.png')
        scaled_bg = pygame.transform.scale(bg_img, (WIN_WIDTH, WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))

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

    def show_profiles(self, surface):
        """Displays player and opponent profiles"""
        opponent_img = pygame.image.load('assets/borders/opponent_img.png')
        player_img = pygame.image.load('assets/borders/player_img.png')
        player_x = (WIN_WIDTH - player_img.get_width()) + 30
        player_y = (WIN_HEIGHT - player_img.get_height()) + 70

        opponent_name_tag = pygame.image.load('assets/borders/rectangle_border.png')
        scale_tag_opp = pygame.transform.scale(opponent_name_tag, (350, 60))
        player_name_tag = pygame.image.load('assets/borders/rectangle_border.png')
        scale_tag_play = pygame.transform.scale(player_name_tag, (350, 60))
        dag_x = (WIN_WIDTH - scale_tag_play.get_width()) - 130
        dag_y = (WIN_HEIGHT - scale_tag_play.get_height())

        op_profile_img = pygame.image.load('assets/profile_pictures/profile_default.png')
        scale_op_pic = pygame.transform.scale(op_profile_img, (150, 150))
        pl_profile_img = pygame.image.load('assets/profile_pictures/profile_default_2.png')
        scale_ppic = pygame.transform.scale(pl_profile_img, (150, 150))
        ppic_x = (WIN_WIDTH - scale_ppic.get_width()) - 20
        ppic_y = (WIN_HEIGHT - scale_ppic.get_height())

        surface.blit(scale_op_pic, (20, -20))
        surface.blit(scale_ppic, (ppic_x, ppic_y))
        surface.blit(scale_tag_opp, (130, 7))
        surface.blit(scale_tag_play, (dag_x, dag_y))
        surface.blit(opponent_img, (-30, -70))
        surface.blit(player_img, (player_x, player_y))

    def show_timer(self, surface):
        """Displays the timer"""
        timer_border = pygame.image.load('assets/borders/rectangle_border.png')
        scale_timer = pygame.transform.scale(timer_border, (180, 140))
        timer_y = (WIN_HEIGHT - scale_timer.get_height()) -80
        surface.blit(scale_timer, (45, timer_y))

    def show_menu_button(self, surface):
        """Draw menu button and timer"""
        menu_button = pygame.image.load('assets/buttons/menu_button_small.png')
        rect_menu_button = menu_button.get_rect()
        rect_menu_button.center = (WIN_WIDTH - 100, 100)
        surface.blit(menu_button, rect_menu_button)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_menu_button.collidepoint(event.pos):
                    self.set_menu_state(True)

    def show_game_menu(self, surface):
        """Displays the in game menu"""
        game_menu = pygame.image.load('assets/menus/coc_menu.png')
        scaled_game_menu = pygame.transform.scale(game_menu, (WIN_WIDTH // 2.3, WIN_HEIGHT // 1.2))
        game_menu_x = (WIN_WIDTH - scaled_game_menu.get_width()) // 2
        game_menu_y = (WIN_HEIGHT - scaled_game_menu.get_height()) // 2

        # This is the underline for menu selection
        underline_surrender = pygame.image.load('assets/menus/underline.png')
        underline_surrender.set_alpha(0)
        underline_continue = pygame.image.load('assets/menus/underline.png')
        underline_continue.set_alpha(0)
        underline_setts = pygame.image.load('assets/menus/underline.png')
        underline_setts.set_alpha(0)

        # Display text of main menu
        font = pygame.font.Font('freesansbold.ttf', 32)
        menu_setts = font.render('Settings', True, (220, 50, 50), None)
        setts_rect = menu_setts.get_rect()
        setts_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50)

        menu_surrender = font.render('Surrender', True, (220, 50, 50), None)
        surrender_rect = menu_surrender.get_rect()
        surrender_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 100)

        menu_continue = font.render('Continue', True, (220, 50, 50), None)
        continue_rect = menu_continue.get_rect()
        continue_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 150)

        setts_line = menu_setts.get_rect()
        setts_line.center = (WIN_WIDTH // 2 - 15, WIN_HEIGHT // 2 + 75)
        surrender_line = menu_setts.get_rect()
        surrender_line.center = (WIN_WIDTH // 2 - 15, WIN_HEIGHT // 2 + 125)
        continue_line = menu_setts.get_rect()
        continue_line.center = (WIN_WIDTH // 2 - 15, WIN_HEIGHT // 2 + 175)

        surface.blit(scaled_game_menu, (game_menu_x, game_menu_y))

        # Draw the text
        surface.blit(menu_setts, setts_rect)
        surface.blit(menu_surrender, surrender_rect)
        surface.blit(menu_continue, continue_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_menu_state(False)

                if setts_rect.collidepoint(event.pos):
                    # Button clicked!
                    pass

                if surrender_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_menu_state(False)
                    self.set_play(False)

        # Check if the mouse is hovering over the text rectangle
        if setts_rect.collidepoint(pygame.mouse.get_pos()):
            underline_setts.set_alpha(255)
            surface.blit(underline_setts, setts_line)
        else:
            underline_setts.set_alpha(0)
            surface.blit(underline_setts, setts_line)

        if surrender_rect.collidepoint(pygame.mouse.get_pos()):
            underline_surrender.set_alpha(255)
            surface.blit(underline_surrender, surrender_line)
        else:
            underline_surrender.set_alpha(0)
            surface.blit(underline_surrender, surrender_line)

        if continue_rect.collidepoint(pygame.mouse.get_pos()):
            underline_continue.set_alpha(255)
            surface.blit(underline_continue, continue_line)
        else:
            underline_continue.set_alpha(0)
            surface.blit(underline_continue, continue_line)