#!/usr/bin/python3
"""Knight module"""

import pygame

from pieces.Piece import Piece


class Knight(Piece):
	"""Knight class that inherits from Piece"""
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		img_path = 'assets/chess_pieces/' + color[0] + '_knight_front.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 20, board.square_height - 20))

		self.notation = 'N'


	def get_possible_moves(self, board):
		"""Gets the possible moves this chess piece can make"""
		output = []
		moves = [
			(1, -2),
			(2, -1),
			(2, 1),
			(1, 2),
			(-1, 2),
			(-2, 1),
			(-2, -1),
			(-1, -2)
		]

		for move in moves:
			new_pos = (self.x + move[0], self.y + move[1])
			if (
				new_pos[0] < 8 and
				new_pos[0] >= 0 and 
				new_pos[1] < 8 and 
				new_pos[1] >= 0
			):
				output.append([
					board.get_square_from_pos(
						new_pos
					)
				])

		return output