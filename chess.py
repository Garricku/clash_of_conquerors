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