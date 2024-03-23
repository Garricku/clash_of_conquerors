#!/usr/bin/python3
"""The chess game logic module Chess class"""

import pygame

from const import *
"""Import the constants"""


class Chess():
    """Chess class inherits from Game"""
    def __init__(self):
        """Initialize the chess game logic base variables"""
        screen_info = pygame.display.Info()
        self.WIN_WIDTH = screen_info.current_w
        self.WIN_HEIGHT = screen_info.current_h
        self.chess_theme = 'assets/chess_board/chess_table_v4.png'
        chessboard_img = pygame.image.load(self.chess_theme)
        scaled_chessboard_img = pygame.transform.scale(chessboard_img, (self.WIN_WIDTH // 1.3, self.WIN_HEIGHT // 1.2))
        A1_x = (self.WIN_WIDTH - scaled_chessboard_img.get_width()) // 2 + 130
        A1_y = 98
        self.A1_rect = pygame.Rect(A1_x, A1_y, 93, 55)

    def show_chessboard(self, surface):
        """Displays the chessboard"""
        # Calculate the starting position to center the chessboard
        chessboard_img = pygame.image.load(self.chess_theme)
        scaled_chessboard_img = pygame.transform.scale(chessboard_img, (self.WIN_WIDTH // 1.3, self.WIN_HEIGHT // 1.2))
        surface.blit(scaled_chessboard_img, ((self.WIN_WIDTH - scaled_chessboard_img.get_width()) // 2 + 20, 50))

        black = (0, 0, 0)
        white = (255, 255, 255)

        if (ROWS + COLS) % 2 == 0:
            color = black
        else:
            color = white
        pygame.draw.rect(surface, color, self.A1_rect)