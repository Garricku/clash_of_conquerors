#!/usr/bin/python3
"""The chess game logic module Chess class"""

import pygame
import time

from const import *
"""Import the constants"""


class Chess():
    """Chess class inherits from Game"""
    def __init__(self):
        """Initialize the chess game logic base variables"""
        self.clock = pygame.time.Clock()
        screen_info = pygame.display.Info()
        self.WIN_WIDTH = screen_info.current_w
        self.WIN_HEIGHT = screen_info.current_h
        self.chess_theme = 'assets/chess_board/chess_table_v4.png'
        chessboard_img = pygame.image.load(self.chess_theme)
        scaled_chessboard_img = pygame.transform.scale(chessboard_img, (self.WIN_WIDTH // 1.3, self.WIN_HEIGHT // 1.2))
        A8_x = (self.WIN_WIDTH - scaled_chessboard_img.get_width()) // 2 + 131
        A8_y = 98
        self.A8_rect = pygame.Rect(A8_x, A8_y, 90, 55)
        self.B8_rect = pygame.Rect(A8_x + 95, A8_y, 90, 55)
        self.C8_rect = pygame.Rect(A8_x + 191, A8_y, 90, 55)
        self.D8_rect = pygame.Rect(A8_x + 287, A8_y, 90, 55)
        self.E8_rect = pygame.Rect(A8_x + 382, A8_y, 90, 55)
        self.F8_rect = pygame.Rect(A8_x + 478, A8_y, 90, 55)
        self.G8_rect = pygame.Rect(A8_x + 573, A8_y, 90, 55)
        self.H8_rect = pygame.Rect(A8_x + 668, A8_y, 90, 55)
        self.A7_rect = pygame.Rect(A8_x - 4, A8_y + 57, 90, 55)
        self.B7_rect = pygame.Rect(A8_x + 92, A8_y + 57, 90, 55)
        self.C7_rect = pygame.Rect(A8_x + 189, A8_y + 57, 90, 55)
        self.D7_rect = pygame.Rect(A8_x + 285, A8_y + 57, 90, 55)
        self.E7_rect = pygame.Rect(A8_x + 381, A8_y + 57, 90, 55)
        self.F7_rect = pygame.Rect(A8_x + 478, A8_y + 57, 90, 55)
        self.G7_rect = pygame.Rect(A8_x + 574, A8_y + 57, 90, 55)
        self.H7_rect = pygame.Rect(A8_x + 670, A8_y + 57, 90, 55)

    def show_chessboard(self, surface):
        """Displays the chessboard"""
        # Calculate the starting position to center the chessboard
        chessboard_img = pygame.image.load(self.chess_theme)
        scaled_chessboard_img = pygame.transform.scale(chessboard_img, (self.WIN_WIDTH // 1.3, self.WIN_HEIGHT // 1.2))
        surface.blit(scaled_chessboard_img, ((self.WIN_WIDTH - scaled_chessboard_img.get_width()) // 2 + 20, 50))
        
        yellow = (250, 250, 100, 255)
        pygame.draw.rect(surface, yellow, self.A8_rect)
        pygame.draw.rect(surface, yellow, self.B8_rect)
        pygame.draw.rect(surface, yellow, self.C8_rect)
        pygame.draw.rect(surface, yellow, self.D8_rect)
        pygame.draw.rect(surface, yellow, self.E8_rect)
        pygame.draw.rect(surface, yellow, self.F8_rect)
        pygame.draw.rect(surface, yellow, self.G8_rect)
        pygame.draw.rect(surface, yellow, self.H8_rect)
        pygame.draw.rect(surface, yellow, self.A7_rect)
        pygame.draw.rect(surface, yellow, self.B7_rect)
        pygame.draw.rect(surface, yellow, self.C7_rect)
        pygame.draw.rect(surface, yellow, self.D7_rect)
        pygame.draw.rect(surface, yellow, self.E7_rect)
        pygame.draw.rect(surface, yellow, self.F7_rect)
        pygame.draw.rect(surface, yellow, self.G7_rect)
        pygame.draw.rect(surface, yellow, self.H7_rect)

    def blink_tile(self, surface, rect):
        """Causes a yellow blinking effect on a rect"""
        # This method does not work yet!
        opacity = 0
        yellow = (250, 250, 100, opacity) # The color starts off invisible
        while opacity <= 255:
            pygame.draw.rect(surface, yellow, rect)
            opacity += 5
        while opacity >= 0:
            pygame.draw.rect(surface, yellow, rect)
            opacity -= 5