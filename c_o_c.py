#!/usr/bin/python3
"""c_o_c - Clash of Conquerors game"""

import pygame
import sys

from const import *
from chess import Game
from main import Main
"""Import the constants and the Game class"""


class Chess(Main):
    """Chess class inherits from Main"""

    def play_game(self):
        """plays the game chess screen"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button.collidepoint(event.pos):
                        # Button clicked!
                        pygame.quit()
                        sys.exit()

            # Draw background
            Game.show_game_bg(self.screen)

            # Draw chessboard
            Game.show_chessboard(self.screen)

            # Player and opponent profiles
            # Load buttons and bars
            menu_button = pygame.image.load('assets/buttons/menu_button_small.png')
            bar_x = (WIN_WIDTH - menu_button.get_width()) - 40
            bar_y = (WIN_HEIGHT - menu_button.get_height()) // 9

            # Players profiles
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

            # Timer
            timer_border = pygame.image.load('assets/borders/rectangle_border.png')
            scale_timer = pygame.transform.scale(timer_border, (180, 140))
            timer_y = (WIN_HEIGHT - scale_timer.get_height()) -80
            self.screen.blit(scale_op_pic, (20, -20))
            self.screen.blit(scale_ppic, (ppic_x, ppic_y))
            self.screen.blit(scale_tag_opp, (130, 7))
            self.screen.blit(scale_tag_play, (dag_x, dag_y))
            self.screen.blit(opponent_img, (-30, -70))
            self.screen.blit(player_img, (player_x, player_y))

            # Draw menu button and timer
            self.screen.blit(menu_button, (bar_x, bar_y))
            self.screen.blit(scale_timer, (45, timer_y))

            Game.show_cursor(self.screen)

            # Keep display updated
            pygame.display.update()