#!/usr/bin/python3
"""The chess game logic module Chess class"""

import pygame

from pieces.Square import Square
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Queen import Queen
from pieces.King import King
from pieces.Pawn import Pawn

from const import *
"""Import the constants"""


class Board:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.square_width = width // 8
		self.square_height = height // 8
		self.selected_piece = None
		self.turn = 'white'
    screen_info = pygame.display.Info()
    self.WIN_WIDTH = screen_info.current_w
    self.WIN_HEIGHT = screen_info.current_h
    self.color_1 = (255, 255, 255)
    self.color_2 = (0, 0, 0)

		self.config = [
			['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
			['b ', 'b ', 'b ', 'b ', 'b ', 'b ', 'b ', 'b '],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['','','','','','','',''],
			['w ', 'w ', 'w ', 'w ', 'w ', 'w ', 'w ', 'w '],
			['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
		]

		self.squares = self.generate_squares()

		self.setup_board()

	def generate_squares(self):
		output = []
		for y in range(8):
			for x in range(8):
				output.append(
					Square(
						x,
						y,
						self.square_width,
						self.square_height
					)
				)

		return output


	def setup_board(self):
		for y, row in enumerate(self.config):
			for x, piece in enumerate(row):
				if piece != '':
					square = self.get_square_from_pos((x, y))

					if piece[1] == 'R':
						square.occupying_piece = Rook(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == 'N':
						square.occupying_piece = Knight(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == 'B':
						square.occupying_piece = Bishop(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == 'Q':
						square.occupying_piece = Queen(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == 'K':
						square.occupying_piece = King(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)

					elif piece[1] == ' ':
						square.occupying_piece = Pawn(
							(x, y),
							'white' if piece[0] == 'w' else 'black',
							self
						)


	def handle_click(self, mx, my):
		x = mx // self.square_width
		y = my // self.square_height
		clicked_square = self.get_square_from_pos((x, y))

		if self.selected_piece is None:
			if clicked_square.occupying_piece is not None:
				if clicked_square.occupying_piece.color == self.turn:
					self.selected_piece = clicked_square.occupying_piece

		elif self.selected_piece.move(self, clicked_square):
			self.turn = 'white' if self.turn == 'black' else 'black'

		elif clicked_square.occupying_piece is not None:
			if clicked_square.occupying_piece.color == self.turn:
				self.selected_piece = clicked_square.occupying_piece


	def is_in_check(self, color, board_change=None): # board_change = [(x1, y1), (x2, y2)]
		output = False
		king_pos = None

		changing_piece = None
		old_square = None
		new_square = None
		new_square_old_piece = None

		if board_change is not None:
			for square in self.squares:
				if square.pos == board_change[0]:
					changing_piece = square.occupying_piece
					old_square = square
					old_square.occupying_piece = None
			for square in self.squares:
				if square.pos == board_change[1]:
					new_square = square
					new_square_old_piece = new_square.occupying_piece
					new_square.occupying_piece = changing_piece

		pieces = [
			i.occupying_piece for i in self.squares if i.occupying_piece is not None
		]

		if changing_piece is not None:
			if changing_piece.notation == 'K':
				king_pos = new_square.pos
		if king_pos == None:
			for piece in pieces:
				if piece.notation == 'K':
					if piece.color == color:
						king_pos = piece.pos
		for piece in pieces:
			if piece.color != color:
				for square in piece.attacking_squares(self):
					if square.pos == king_pos:
						output = True

		if board_change is not None:
			old_square.occupying_piece = changing_piece
			new_square.occupying_piece = new_square_old_piece
						
		return output


	def is_in_checkmate(self, color):
		output = False

		for piece in [i.occupying_piece for i in self.squares]:
			if piece != None:
				if piece.notation == 'K' and piece.color == color:
					king = piece

		if king.get_valid_moves(self) == []:
			if self.is_in_check(color):
				output = True

		return output


	def get_square_from_pos(self, pos):
		for square in self.squares:
			if (square.x, square.y) == (pos[0], pos[1]):
				return square


	def get_piece_from_pos(self, pos):
		return self.get_square_from_pos(pos).occupying_piece


	def draw(self, display):
		if self.selected_piece is not None:
			self.get_square_from_pos(self.selected_piece.pos).highlight = True
			for square in self.selected_piece.get_valid_moves(self):
				square.highlight = True

		for square in self.squares:
			square.draw(display)
        
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
                square_color = self.color_1 if (i + j) % 2 == 0 else self.color_2
            
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

    def color_1_to_white(self):
        """Changes one of the color pair of the tiles white by default"""
        self.color_1 = (255, 255, 255)

    def color_1_to_pink(self):
        """Changes one of the color pair of the tiles white by default"""
        self.color_1 = (255, 192, 203)

    def color_1_to_blue(self):
        """Changes one of the color pair of the tiles white by default"""
        self.color_1 = (60, 60, 255)

    def color_2_to_black(self):
        """Changes one of the color pair of the tiles black by default"""
        self.color_2 = (0, 0, 0)

    def color_2_to_purple(self):
        """Changes one of the color pair of the tiles black by default"""
        self.color_2 = (128, 0, 128)

    def color_2_to_red(self):
        """Changes one of the color pair of the tiles black by default"""
        self.color_2 = (255, 60, 60)