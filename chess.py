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
        screen_info = pygame.display.Info()
        self.WIN_WIDTH = screen_info.current_w
        self.WIN_HEIGHT = screen_info.current_h
        self.chess_theme = 'assets/chess_board/chess_table_v4.png'
        chessboard_img = pygame.image.load(self.chess_theme)
        scaled_chessboard_img = pygame.transform.scale(chessboard_img, (self.WIN_WIDTH // 1.3, self.WIN_HEIGHT // 1.2))
        A8_x = (self.WIN_WIDTH - scaled_chessboard_img.get_width()) // 2 + 131
        A8_y = 98
        # Row 1 starting from the top
        # I put them here in init method so that they can be accessible by
        # other methods that may be defined later that need these variables
        self.A8_rect = pygame.Rect(A8_x, A8_y, 90, 55)
        self.B8_rect = pygame.Rect(A8_x + 95, A8_y, 90, 55)
        self.C8_rect = pygame.Rect(A8_x + 191, A8_y, 90, 55)
        self.D8_rect = pygame.Rect(A8_x + 287, A8_y, 90, 55)
        self.E8_rect = pygame.Rect(A8_x + 381, A8_y, 90, 55)
        self.F8_rect = pygame.Rect(A8_x + 478, A8_y, 90, 55)
        self.G8_rect = pygame.Rect(A8_x + 573, A8_y, 90, 55)
        self.H8_rect = pygame.Rect(A8_x + 668, A8_y, 90, 55)
        # Row 2
        self.A7_rect = pygame.Rect(A8_x - 4, A8_y + 57, 90, 55)
        self.B7_rect = pygame.Rect(A8_x + 92, A8_y + 57, 90, 55)
        self.C7_rect = pygame.Rect(A8_x + 189, A8_y + 57, 90, 55)
        self.D7_rect = pygame.Rect(A8_x + 285, A8_y + 57, 90, 55)
        self.E7_rect = pygame.Rect(A8_x + 381, A8_y + 57, 90, 55)
        self.F7_rect = pygame.Rect(A8_x + 478, A8_y + 57, 90, 55)
        self.G7_rect = pygame.Rect(A8_x + 574, A8_y + 57, 90, 55)
        self.H7_rect = pygame.Rect(A8_x + 670, A8_y + 57, 90, 55)
        # row 3
        self.A6_rect = pygame.Rect(A8_x - 7, A8_y + 114, 90, 55)
        self.B6_rect = pygame.Rect(A8_x + 90, A8_y + 114, 90, 55)
        self.C6_rect = pygame.Rect(A8_x + 187, A8_y + 114, 90, 55)
        self.D6_rect = pygame.Rect(A8_x + 284, A8_y + 114, 90, 55)
        self.E6_rect = pygame.Rect(A8_x + 381, A8_y + 114, 90, 55)
        self.F6_rect = pygame.Rect(A8_x + 478, A8_y + 114, 90, 55)
        self.G6_rect = pygame.Rect(A8_x + 575, A8_y + 114, 90, 55)
        self.H6_rect = pygame.Rect(A8_x + 672, A8_y + 114, 90, 55)
        # row 4
        self.A5_rect = pygame.Rect(A8_x - 10, A8_y + 172, 90, 55)
        self.B5_rect = pygame.Rect(A8_x + 87, A8_y + 172, 90, 55)
        self.C5_rect = pygame.Rect(A8_x + 185, A8_y + 172, 90, 55)
        self.D5_rect = pygame.Rect(A8_x + 282, A8_y + 172, 90, 55)
        self.E5_rect = pygame.Rect(A8_x + 381, A8_y + 172, 90, 55)
        self.F5_rect = pygame.Rect(A8_x + 478, A8_y + 172, 90, 55)
        self.G5_rect = pygame.Rect(A8_x + 576, A8_y + 172, 90, 55)
        self.H5_rect = pygame.Rect(A8_x + 673, A8_y + 172, 90, 55)
        # row 5
        self.A4_rect = pygame.Rect(A8_x - 12, A8_y + 232, 90, 55)
        self.B4_rect = pygame.Rect(A8_x + 87, A8_y + 232, 90, 55)
        self.C4_rect = pygame.Rect(A8_x + 185, A8_y + 232, 90, 55)
        self.D4_rect = pygame.Rect(A8_x + 284, A8_y + 232, 90, 55)
        self.E4_rect = pygame.Rect(A8_x + 381, A8_y + 232, 90, 55)
        self.F4_rect = pygame.Rect(A8_x + 480, A8_y + 232, 90, 55)
        self.G4_rect = pygame.Rect(A8_x + 578, A8_y + 232, 90, 55)
        self.H4_rect = pygame.Rect(A8_x + 677, A8_y + 232, 90, 55)
        # row 6
        self.A3_rect = pygame.Rect(A8_x - 15, A8_y + 292, 90, 55)
        self.B3_rect = pygame.Rect(A8_x + 84, A8_y + 292, 90, 55)
        self.C3_rect = pygame.Rect(A8_x + 183, A8_y + 292, 90, 55)
        self.D3_rect = pygame.Rect(A8_x + 282, A8_y + 292, 90, 55)
        self.E3_rect = pygame.Rect(A8_x + 381, A8_y + 292, 90, 55)
        self.F3_rect = pygame.Rect(A8_x + 480, A8_y + 292, 90, 55)
        self.G3_rect = pygame.Rect(A8_x + 580, A8_y + 292, 90, 55)
        self.H3_rect = pygame.Rect(A8_x + 679, A8_y + 292, 90, 55)
        # row 7
        self.A2_rect = pygame.Rect(A8_x - 19, A8_y + 354, 90, 55)
        self.B2_rect = pygame.Rect(A8_x + 81, A8_y + 354, 90, 55)
        self.C2_rect = pygame.Rect(A8_x + 181, A8_y + 354, 90, 55)
        self.D2_rect = pygame.Rect(A8_x + 281, A8_y + 354, 90, 55)
        self.E2_rect = pygame.Rect(A8_x + 380, A8_y + 354, 90, 55)
        self.F2_rect = pygame.Rect(A8_x + 481, A8_y + 354, 90, 55)
        self.G2_rect = pygame.Rect(A8_x + 581, A8_y + 354, 90, 55)
        self.H2_rect = pygame.Rect(A8_x + 682, A8_y + 354, 90, 55)
        # row 8 Last row
        self.A1_rect = pygame.Rect(A8_x - 23, A8_y + 415, 90, 55)
        self.B1_rect = pygame.Rect(A8_x + 78, A8_y + 415, 90, 55)
        self.C1_rect = pygame.Rect(A8_x + 180, A8_y + 415, 90, 55)
        self.D1_rect = pygame.Rect(A8_x + 280, A8_y + 415, 90, 55)
        self.E1_rect = pygame.Rect(A8_x + 381, A8_y + 415, 90, 55)
        self.F1_rect = pygame.Rect(A8_x + 480, A8_y + 415, 90, 55)
        self.G1_rect = pygame.Rect(A8_x + 583, A8_y + 415, 90, 55)
        self.H1_rect = pygame.Rect(A8_x + 682, A8_y + 415, 90, 55)

    def show_chessboard(self, surface):
        """Displays the chessboard"""
        # Calculate the starting position to center the chessboard
        chessboard_img = pygame.image.load(self.chess_theme)
        scaled_chessboard_img = pygame.transform.scale(chessboard_img, (self.WIN_WIDTH // 1.3, self.WIN_HEIGHT // 1.2))
        surface.blit(scaled_chessboard_img, ((self.WIN_WIDTH - scaled_chessboard_img.get_width()) // 2 + 20, 50))
        
        yellow = (250, 250, 100, 255)
        # These are the rectangles that will help identify and blink yellow
        # on blocks that are possible moves also for move confirmation turn green
        # row 1 starting from the top
        pygame.draw.rect(surface, yellow, self.A8_rect)
        pygame.draw.rect(surface, yellow, self.B8_rect)
        pygame.draw.rect(surface, yellow, self.C8_rect)
        pygame.draw.rect(surface, yellow, self.D8_rect)
        pygame.draw.rect(surface, yellow, self.E8_rect)
        pygame.draw.rect(surface, yellow, self.F8_rect)
        pygame.draw.rect(surface, yellow, self.G8_rect)
        pygame.draw.rect(surface, yellow, self.H8_rect)
        # row two 
        pygame.draw.rect(surface, yellow, self.A7_rect)
        pygame.draw.rect(surface, yellow, self.B7_rect)
        pygame.draw.rect(surface, yellow, self.C7_rect)
        pygame.draw.rect(surface, yellow, self.D7_rect)
        pygame.draw.rect(surface, yellow, self.E7_rect)
        pygame.draw.rect(surface, yellow, self.F7_rect)
        pygame.draw.rect(surface, yellow, self.G7_rect)
        pygame.draw.rect(surface, yellow, self.H7_rect)
        # row 3
        pygame.draw.rect(surface, yellow, self.A6_rect)
        pygame.draw.rect(surface, yellow, self.B6_rect)
        pygame.draw.rect(surface, yellow, self.C6_rect)
        pygame.draw.rect(surface, yellow, self.D6_rect)
        pygame.draw.rect(surface, yellow, self.E6_rect)
        pygame.draw.rect(surface, yellow, self.F6_rect)
        pygame.draw.rect(surface, yellow, self.G6_rect)
        pygame.draw.rect(surface, yellow, self.H6_rect)
        # row 4
        pygame.draw.rect(surface, yellow, self.A5_rect)
        pygame.draw.rect(surface, yellow, self.B5_rect)
        pygame.draw.rect(surface, yellow, self.C5_rect)
        pygame.draw.rect(surface, yellow, self.D5_rect)
        pygame.draw.rect(surface, yellow, self.E5_rect)
        pygame.draw.rect(surface, yellow, self.F5_rect)
        pygame.draw.rect(surface, yellow, self.G5_rect)
        pygame.draw.rect(surface, yellow, self.H5_rect)
        #row 5
        pygame.draw.rect(surface, yellow, self.A4_rect)
        pygame.draw.rect(surface, yellow, self.B4_rect)
        pygame.draw.rect(surface, yellow, self.C4_rect)
        pygame.draw.rect(surface, yellow, self.D4_rect)
        pygame.draw.rect(surface, yellow, self.E4_rect)
        pygame.draw.rect(surface, yellow, self.F4_rect)
        pygame.draw.rect(surface, yellow, self.G4_rect)
        pygame.draw.rect(surface, yellow, self.H4_rect)
        #row 6
        pygame.draw.rect(surface, yellow, self.A3_rect)
        pygame.draw.rect(surface, yellow, self.B3_rect)
        pygame.draw.rect(surface, yellow, self.C3_rect)
        pygame.draw.rect(surface, yellow, self.D3_rect)
        pygame.draw.rect(surface, yellow, self.E3_rect)
        pygame.draw.rect(surface, yellow, self.F3_rect)
        pygame.draw.rect(surface, yellow, self.G3_rect)
        pygame.draw.rect(surface, yellow, self.H3_rect)
        # row 7
        pygame.draw.rect(surface, yellow, self.A2_rect)
        pygame.draw.rect(surface, yellow, self.B2_rect)
        pygame.draw.rect(surface, yellow, self.C2_rect)
        pygame.draw.rect(surface, yellow, self.D2_rect)
        pygame.draw.rect(surface, yellow, self.E2_rect)
        pygame.draw.rect(surface, yellow, self.F2_rect)
        pygame.draw.rect(surface, yellow, self.G2_rect)
        pygame.draw.rect(surface, yellow, self.H2_rect)
        # row 8 this is the last row
        pygame.draw.rect(surface, yellow, self.A1_rect)
        pygame.draw.rect(surface, yellow, self.B1_rect)
        pygame.draw.rect(surface, yellow, self.C1_rect)
        pygame.draw.rect(surface, yellow, self.D1_rect)
        pygame.draw.rect(surface, yellow, self.E1_rect)
        pygame.draw.rect(surface, yellow, self.F1_rect)
        pygame.draw.rect(surface, yellow, self.G1_rect)
        pygame.draw.rect(surface, yellow, self.H1_rect)

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