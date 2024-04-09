#!/usr/bin/python3
"""This is the chess game screen module"""

import pygame
import sys
# import time

from const import *
from chess import Chess
"""Imports the constants"""


class Game():
    """The class for the chess game screen"""
    def __init__(self):
        """Initialize the attributes"""
        self.play = False
        self.opt = False
        self.help = False
        self.menu_state = False
        screen_info = pygame.display.Info()
        self.WIN_WIDTH = screen_info.current_w
        self.WIN_HEIGHT = screen_info.current_h
        self.chess = Chess()
        # self.t = 10 This was meant for the timer, but issues arise

    def get_win_width(self):
        """Returns the window width"""
        return self.WIN_WIDTH

    def get_win_height(self):
        """Returns the window height"""
        return self.WIN_HEIGHT

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
        scaled_bg = pygame.transform.scale(bg_img, (self.WIN_WIDTH, self.WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))

    def show_main_menu(self, surface):
        """Displays the main menu"""
        # Load the main menu
        main_menu = pygame.image.load('assets/menus/menu_list.png')
        main_menu.set_alpha(240)
        scaled_main_menu = pygame.transform.scale(main_menu, (self.WIN_WIDTH // 2.3, self.WIN_HEIGHT // 1.2))
        menu_x = (self.WIN_WIDTH - scaled_main_menu.get_width()) // 2
        menu_y = (self.WIN_HEIGHT - scaled_main_menu.get_height()) // 2
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
        text = font.render('PLAY', True, (60, 60, 60), None)
        textRect = text.get_rect()
        textRect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2)

        menu_opt = font.render('SETTINGS', True, (60, 60, 60), None)
        opt_rect = menu_opt.get_rect()
        opt_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 50)

        menu_help = font.render('TUTORIAL', True, (60, 60, 60), None)
        help_rect = menu_help.get_rect()
        help_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 100)

        menu_exit = font.render('EXIT', True, (60, 60, 60), None)
        exit_rect = menu_exit.get_rect()
        exit_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 150)

        play_line = text.get_rect()
        play_line.center = (self.WIN_WIDTH // 2 - 44, self.WIN_HEIGHT // 2 + 25)
        opt_line = menu_opt.get_rect()
        opt_line.center = (self.WIN_WIDTH // 2 - 2, self.WIN_HEIGHT // 2 + 75)
        help_line = menu_opt.get_rect()
        help_line.center = (self.WIN_WIDTH // 2 - 2, self.WIN_HEIGHT // 2 + 125)
        exit_line = menu_opt.get_rect()
        exit_line.center = (self.WIN_WIDTH // 2 - 4, self.WIN_HEIGHT // 2 + 175)

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
        cursor_image = pygame.image.load('assets/cursors/custom_cursor.png')
        # Hide default cursor
        pygame.mouse.set_visible(False)
        # Draw custom cursor
        cursor_rect = cursor_image.get_rect(center=pygame.mouse.get_pos())
        surface.blit(cursor_image, cursor_rect)

    def show_menu_bg(self, surface):
        """Displays the background for menus"""
        bg_img = pygame.image.load('assets/title_screens/title_coc_1.png')
        scaled_bg = pygame.transform.scale(bg_img, (self.WIN_WIDTH, self.WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))

    def fade_out_fade_in(self, surface):
        """Fades out to black for smoother transitions"""
        color = (0, 0, 0) # Black
        visibility = 0 # Invisible
        while visibility <= 255:
            surface.fill(color, (visibility))
            visibility += 5 # Increase visibility till fully black
        while visibility >= 0:
            surface.fill(color, (visibility))
            visibility -= 5 # Decrease the visibility till no black

    def show_settings(self, surface):
        """Displays the settings menu"""
        set_off = pygame.image.load('assets/buttons/settings_off.png')
        scale_off = pygame.transform.scale(set_off, (40, 40))
        set_on = pygame.image.load('assets/buttons/settings_on.png')
        scale_on = pygame.transform.scale(set_on, (40, 40))
        font = pygame.font.Font('freesansbold.ttf', 32)
        settings_display = pygame.image.load('assets/borders/timer_border_2.png')
        scaled_setts = pygame.transform.scale(settings_display, (self.WIN_WIDTH, self.WIN_HEIGHT - 70))
        underline_back = pygame.image.load('assets/menus/underline.png')
        underline_back.set_alpha(0)
        menu_back = font.render('RETURN', True, (160, 160, 160), None)
        back_rect = menu_back.get_rect()
        back_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 210)
        back_line = menu_back.get_rect()
        back_line.center = (self.WIN_WIDTH // 2 - 19, self.WIN_HEIGHT // 2 + 235)

        # Color options for themes
        # these are the headings
        themes = font.render('THEMES', True, (160, 160, 160), None)
        themes_rect = themes.get_rect()
        themes_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 - 170)
        color_1 = font.render('Color 1:', True, (160, 160, 160), None)
        color_1_rect = color_1.get_rect()
        color_1_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 - 90)
        color_2 = font.render('Color 2:', True, (160, 160, 160), None)
        color_2_rect = color_2.get_rect()
        color_2_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 20)

        # Theses are the options
        white_text = font.render('White', True, (160, 160, 160), None)
        white_rect = white_text.get_rect()
        white_rect.center = (self.WIN_WIDTH // 2 - 300, self.WIN_HEIGHT // 2 - 40)
        pink_text = font.render('Pink', True, (160, 160, 160), None)
        pink_rect = pink_text.get_rect()
        pink_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 - 40)
        blue_text = font.render('Blue', True, (160, 160, 160), None)
        blue_rect = blue_text.get_rect()
        blue_rect.center = (self.WIN_WIDTH // 2 + 300, self.WIN_HEIGHT // 2 - 40)
        black_text = font.render('Black', True, (160, 160, 160), None)
        black_rect = black_text.get_rect()
        black_rect.center = (self.WIN_WIDTH // 2 - 300, self.WIN_HEIGHT // 2 + 70)
        purple_text = font.render('Purple', True, (160, 160, 160), None)
        purple_rect = purple_text.get_rect()
        purple_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 70)
        red_text = font.render('Red', True, (160, 160, 160), None)
        red_rect = red_text.get_rect()
        red_rect.center = (self.WIN_WIDTH // 2 + 300, self.WIN_HEIGHT // 2 + 70)


        # Display them all
        surface.blit(scaled_setts, (0, 50))
        surface.blit(menu_back, back_rect)
        surface.blit(themes, themes_rect)
        surface.blit(color_1, color_1_rect)
        surface.blit(white_text, white_rect)
        surface.blit(pink_text, pink_rect)
        surface.blit(blue_text, blue_rect)
        surface.blit(color_2, color_2_rect)
        surface.blit(black_text, black_rect)
        surface.blit(purple_text, purple_rect)
        surface.blit(red_text, red_rect)

        if self.chess.color_1 == (255, 255, 255):
            surface.blit(scale_on, (self.WIN_WIDTH // 2 - 150, self.WIN_HEIGHT // 2 - 55))
        else:
            surface.blit(scale_off, (self.WIN_WIDTH // 2 - 150, self.WIN_HEIGHT // 2 - 55))
        
        if self.chess.color_1 == (255, 192, 203):
            surface.blit(scale_on, (self.WIN_WIDTH // 2 + 100, self.WIN_HEIGHT // 2 - 55))
        else:
            surface.blit(scale_off, (self.WIN_WIDTH // 2 + 100, self.WIN_HEIGHT // 2 - 55))

        if self.chess.color_1 == (60, 60, 255):
            surface.blit(scale_on, (self.WIN_WIDTH // 2 + 400, self.WIN_HEIGHT // 2 - 55))
        else:
            surface.blit(scale_off, (self.WIN_WIDTH // 2 + 400, self.WIN_HEIGHT // 2 - 55))

        if self.chess.color_2 == (0, 0, 0):
            surface.blit(scale_on, (self.WIN_WIDTH // 2 - 150, self.WIN_HEIGHT // 2 + 55))
        else:
            surface.blit(scale_off, (self.WIN_WIDTH // 2 - 150, self.WIN_HEIGHT // 2 + 55))

        if self.chess.color_2 == (128, 0, 128):
            surface.blit(scale_on, (self.WIN_WIDTH // 2 + 100, self.WIN_HEIGHT // 2 + 55))
        else:
            surface.blit(scale_off, (self.WIN_WIDTH // 2 + 100, self.WIN_HEIGHT // 2 + 55))

        if self.chess.color_2 == (255, 60, 60):
            surface.blit(scale_on, (self.WIN_WIDTH // 2 + 400, self.WIN_HEIGHT // 2 + 55))
        else:
            surface.blit(scale_off, (self.WIN_WIDTH // 2 + 400, self.WIN_HEIGHT // 2 + 55))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_opt(False)
                
                if white_rect.collidepoint(event.pos):
                    self.chess.color_1_to_white()

                if pink_rect.collidepoint(event.pos):
                    self.chess.color_1_to_pink()

                if blue_rect.collidepoint(event.pos):
                    self.chess.color_1_to_blue()

                if black_rect.collidepoint(event.pos):
                    self.chess.color_2_to_black()

                if purple_rect.collidepoint(event.pos):
                    self.chess.color_2_to_purple()

                if red_rect.collidepoint(event.pos):
                    self.chess.color_2_to_red()

        if back_rect.collidepoint(pygame.mouse.get_pos()):
            underline_back.set_alpha(255)
            surface.blit(underline_back, back_line)
        else:
            underline_back.set_alpha(0)
            surface.blit(underline_back, back_line)

    def show_tutorial(self, surface):
        """Display the how to play screen"""
        font = pygame.font.Font('freesansbold.ttf', 32)
        #settings_display = pygame.image.load('assets/borders/timer_border_2.png')
        #scaled_setts = pygame.transform.scale(settings_display, (self.WIN_WIDTH, self.WIN_HEIGHT - 70))
        underline_back = pygame.image.load('assets/menus/underline.png')
        underline_back.set_alpha(0)
        menu_back = font.render("RETURN", True, (160, 160, 160), None)
        back_rect = menu_back.get_rect()
        back_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 210)
        back_line = menu_back.get_rect()
        back_line.center = (self.WIN_WIDTH // 2 - 19, self.WIN_HEIGHT // 2 + 235)
        tutor_image = pygame.image.load('assets/menus/tutorial_content.png')
        scaled_tutor = pygame.transform.scale(tutor_image, (self.WIN_WIDTH - 200, self.WIN_HEIGHT - 300))

        #surface.blit(scaled_setts, (0, 50))
        surface.blit(menu_back, back_rect)
        surface.blit(scaled_tutor, ((self.WIN_WIDTH - scaled_tutor.get_width()) // 2, (self.WIN_HEIGHT - scaled_tutor.get_height()) // 2.5))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_help(False)

        if back_rect.collidepoint(pygame.mouse.get_pos()):
            underline_back.set_alpha(255)
            surface.blit(underline_back, back_line)
        else:
            underline_back.set_alpha(0)
            surface.blit(underline_back, back_line)

    def show_game_bg(self, surface):
        """
        Displays the in-game background
        Loads the background image
        Resizes it then draws it on the screen
        """
        bg_img = pygame.image.load('assets/backgrounds/background_0.png')
        scaled_bg = pygame.transform.scale(bg_img, (self.WIN_WIDTH, self.WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))

    def show_profiles(self, surface):
        """Displays player and opponent profiles"""
        opponent_img = pygame.image.load('assets/borders/opponent_img.png')
        scale_op_border = pygame.transform.scale(opponent_img, (220, 180))
        player_img = pygame.image.load('assets/borders/opponent_img.png')
        scale_p_border = pygame.transform.scale(player_img, (220, 190))
        player_x = (self.WIN_WIDTH - player_img.get_width() + 55)
        player_y = (self.WIN_HEIGHT - player_img.get_height() + 30)

        opponent_name_tag = pygame.image.load('assets/borders/rectangle_border.png')
        scale_tag_opp = pygame.transform.scale(opponent_name_tag, (200, 90))
        player_name_tag = pygame.image.load('assets/borders/rectangle_border.png')
        scale_tag_play = pygame.transform.scale(player_name_tag, (200, 90))
        dag_x = (self.WIN_WIDTH - scale_tag_play.get_width()) + 15
        dag_y = (self.WIN_HEIGHT - scale_tag_play.get_height()) + 20

        op_profile_img = pygame.image.load('assets/profile_pictures/profile_default_2.png')
        scale_op_pic = pygame.transform.scale(op_profile_img, (130, 120))
        pl_profile_img = pygame.image.load('assets/profile_pictures/profile_default_2.png')
        scale_ppic = pygame.transform.scale(pl_profile_img, (130, 120))
        ppic_x = (self.WIN_WIDTH - scale_ppic.get_width()) - 18
        ppic_y = (self.WIN_HEIGHT - scale_ppic.get_height()) - 65

        # Render the text
        font = pygame.font.Font('freesansbold.ttf', 32)
        text_surface_op = font.render("AI Bot", True, (255, 255, 255))
        text_surface_player = font.render("Player", True, (255, 255, 255))

        surface.blit(scale_op_pic, (18, 20))
        surface.blit(scale_ppic, (ppic_x, ppic_y))
        surface.blit(scale_tag_opp, (-20, 125))
        surface.blit(scale_tag_play, (dag_x, dag_y))
        surface.blit(scale_op_border, (-30, -10))
        surface.blit(scale_p_border, (player_x, player_y))
        # Blit the text surface onto the screen
        surface.blit(text_surface_op, (30, 155))
        surface.blit(text_surface_player, (self.WIN_WIDTH - 135, self.WIN_HEIGHT - 43))

    def show_timer(self, surface):
        """Displays the timer"""
        timer_border = pygame.image.load('assets/borders/rectangle_border.png')
        scale_timer = pygame.transform.scale(timer_border, (180, 140))
        timer_y = (self.WIN_HEIGHT - scale_timer.get_height()) -80
        surface.blit(scale_timer, (45, timer_y))

    def show_menu_button(self, surface):
        """Draw menu button and timer"""
        menu_button = pygame.image.load('assets/buttons/menu_button_small.png')
        rect_menu_button = menu_button.get_rect()
        rect_menu_button.center = (self.WIN_WIDTH - 100, 100)
        surface.blit(menu_button, rect_menu_button)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_menu_button.collidepoint(event.pos):
                    self.set_menu_state(True)

    def show_game_menu(self, surface):
        """Displays the in game menu"""
        game_menu = pygame.image.load('assets/menus/coc_menu.png')
        scaled_game_menu = pygame.transform.scale(game_menu, (self.WIN_WIDTH // 3, self.WIN_HEIGHT // 1.5))
        game_menu_x = (self.WIN_WIDTH - scaled_game_menu.get_width()) // 2
        game_menu_y = (self.WIN_HEIGHT - scaled_game_menu.get_height()) // 2

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
        setts_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 50)

        menu_surrender = font.render('Surrender', True, (220, 50, 50), None)
        surrender_rect = menu_surrender.get_rect()
        surrender_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 100)

        menu_continue = font.render('Continue', True, (220, 50, 50), None)
        continue_rect = menu_continue.get_rect()
        continue_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 150)

        setts_line = menu_setts.get_rect()
        setts_line.center = (self.WIN_WIDTH // 2 - 15, self.WIN_HEIGHT // 2 + 75)
        surrender_line = menu_setts.get_rect()
        surrender_line.center = (self.WIN_WIDTH // 2 - 15, self.WIN_HEIGHT // 2 + 125)
        continue_line = menu_setts.get_rect()
        continue_line.center = (self.WIN_WIDTH // 2 - 15, self.WIN_HEIGHT // 2 + 175)

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
                    self.set_menu_state(False)
                    self.set_opt(True)

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

    def _countdown(self, surface):
        """Timer but it does not work yet issues with fps"""
        while self.t:
            mins, secs = divmod(self.t, 60)
            timer = f"{mins:02d}:{secs:02d}"  # Format as "minutes:seconds"
            font = pygame.font.Font('freesansbold.ttf', 32)
            time_text = font.render(timer, True, (255, 255, 255))
            surface.blit(time_text, (45, self.WIN_HEIGHT - 220))
            # time.sleep(1)  # Wait for 1 second
            self.t -= 1

    def show_tour_bg(self, surface):
        """Shows the tutorial back ground"""
        bg_img = pygame.image.load('assets/title_screens/title_coc_0.png')
        scaled_bg = pygame.transform.scale(bg_img, (self.WIN_WIDTH, self.WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))
