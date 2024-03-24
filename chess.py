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

    white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
    black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                    'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
    black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
    captured_pieces_white = []
    captured_pieces_black = []
    # 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
    turn_step = 0
    selection = 100
    valid_moves = []

    # load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
    black_queen = pygame.image.load('assets/chess_pieces/black_queen.png')
    black_queen = pygame.transform.scale(black_queen, (80, 80))
    black_queen_small = pygame.transform.scale(black_queen, (45, 45))
    black_king = pygame.image.load('assets/chess_pieces/black_king.png')
    black_king = pygame.transform.scale(black_king, (80, 80))
    black_king_small = pygame.transform.scale(black_king, (45, 45))
    black_rook = pygame.image.load('assets/chess_pieces/black_rook.png')
    black_rook = pygame.transform.scale(black_rook, (80, 80))
    black_rook_small = pygame.transform.scale(black_rook, (45, 45))
    black_bishop = pygame.image.load('assets/chess_pieces/black_bishop.png')
    black_bishop = pygame.transform.scale(black_bishop, (80, 80))
    black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
    black_knight = pygame.image.load('assets/chess_pieces/black_knight_front.png')
    black_knight = pygame.transform.scale(black_knight, (80, 80))
    black_knight_small = pygame.transform.scale(black_knight, (45, 45))
    black_pawn = pygame.image.load('assets/chess_pieces/black_pawn.png')
    black_pawn = pygame.transform.scale(black_pawn, (65, 65))
    black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
    white_queen = pygame.image.load('assets/chess_pieces/white_queen.png')
    white_queen = pygame.transform.scale(white_queen, (80, 80))
    white_queen_small = pygame.transform.scale(white_queen, (45, 45))
    white_king = pygame.image.load('assets/chess_pieces/white_king.png')
    white_king = pygame.transform.scale(white_king, (80, 80))
    white_king_small = pygame.transform.scale(white_king, (45, 45))
    white_rook = pygame.image.load('assets/chess_pieces/white_rook.png')
    white_rook = pygame.transform.scale(white_rook, (80, 80))
    white_rook_small = pygame.transform.scale(white_rook, (45, 45))
    white_bishop = pygame.image.load('assets/chess_pieces/white_bishop.png')
    white_bishop = pygame.transform.scale(white_bishop, (80, 80))
    white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
    white_knight = pygame.image.load('assets/chess_pieces/white_knight_back.png')
    white_knight = pygame.transform.scale(white_knight, (80, 80))
    white_knight_small = pygame.transform.scale(white_knight, (45, 45))
    white_pawn = pygame.image.load('assets/chess_pieces/white_pawn.png')
    white_pawn = pygame.transform.scale(white_pawn, (65, 65))
    white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
    white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
    small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                        white_rook_small, white_bishop_small]
    black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
    small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                        black_rook_small, black_bishop_small]
    piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

    def chess_board(self, surface):
    # Calculate the starting position of the chessboard
        square_size = 80
        board_width = 8 * square_size
        board_height = 8 * square_size
        board_x = (self.WIN_WIDTH - board_width) // 2
        board_y = (self.WIN_HEIGHT - board_height) // 2
    
        for i in range(8):
            for j in range(8):
            # Determine the color of the square based on its position
                square_color = 'white' if (i + j) % 2 == 0 else 'black'
            
            # Draw the square
                pygame.draw.rect(surface, square_color, [board_x + j * square_size, board_y + i * square_size, square_size, square_size])

    def draw_pieces(self, surface):
        for i in range(len(self.white_pieces)):
            index = self.piece_list.index(self.white_pieces[i])
            if self.white_pieces[i] == 'pawn':
                surface.blit(self.white_pawn, (self.white_locations[i][0] * 80 + 372, self.white_locations[i][1] * 110 + 30))
            else:
                surface.blit(self.white_images[index], (self.white_locations[i][0] * 80 + 360, self.white_locations[i][1] * 100 + 60))
            if self.turn_step < 2:
                if self.selection == i:
                    pygame.draw.rect(surface, 'purple', [self.white_locations[i][0] * 100 + 1, self.white_locations[i][1] * 100 + 1,
                                                    100, 100], 2)

        for i in range(len(self.black_pieces)):
            index = self.piece_list.index(self.black_pieces[i])
            if self.black_pieces[i] == 'pawn':
                surface.blit(self.black_pawn, (self.black_locations[i][0] * 80 + 372, self.black_locations[i][1] * 85 + 30))
            else:
                surface.blit(self.black_images[index], (self.black_locations[i][0] * 80 + 360, self.black_locations[i][1] * 87 + 10))
            if self.turn_step >= 2:
                if self.selection == i:
                    pygame.draw.rect(surface, 'red', [self.black_locations[i][0] * 100 + 1, self.black_locations[i][1] * 100 + 1,
                                                    100, 100], 2)
