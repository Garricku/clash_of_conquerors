#!/usr/bin/python3
"""Main - Clash of Conquerors game"""

import pygame
import sys

from const import *
from game import Game
from chess import Board
#from chess_piece import ChessPiece
"""Import the constants and the Game class"""


class Main(Game):
    """Main class for game C.O.C."""
    
    def __init__(self):
        """initialize game and display the screen"""
        pygame.init()
        self.game = Game()
        #self.piece = ChessPiece()
        self.screen = pygame.display.set_mode((self.game.WIN_WIDTH, self.game.WIN_HEIGHT))
        pygame.display.set_caption("Clash Of Conquerors")
        # Load and set the icon
        icon_image = pygame.image.load('assets/icons/coc_icon_bigger.png')
        pygame.display.set_icon(icon_image)
    
    def draw(display):
        display.fill('white')

    def mainloop(self):
        """Main game loop"""
        while True:
            while self.game.opt == True: # Setting menu loop starts here
                self.game.show_menu_bg(self.screen)
                self.game.show_settings(self.screen)
                self.game.show_cursor(self.screen)
                pygame.display.update()

            while self.game.help == True: # Tutorial loop
                self.game.show_menu_bg(self.screen)
                self.game.show_tutorial(self.screen)
                self.game.show_cursor(self.screen)
                pygame.display.update()

            while self.game.play == True: # Chess game loop starts here
                self.game.show_game_bg(self.screen)
                #self.chess.show_chessboard(self.screen)
                self.chess.Board(self.screen)
                self.chess.draw_pieces(self.screen)
                self.game.show_profiles(self.screen)
                self.game.show_menu_button(self.screen)
                self.game.show_timer(self.screen)
                self.game.show_cursor(self.screen)
                WINDOW_SIZE = (1000, 1000)
                board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])
                board.draw(self.screen)
                pygame.display.update()

                while self.game.menu_state == True: # This is in the chess game loop
                    self.game.show_menu_bg(self.screen)
                    self.game.show_game_menu(self.screen)
                    self.game.show_cursor(self.screen)
                    pygame.display.update()

                while self.game.opt == True: # This is in the menu loop of chess game loop
                    self.game.show_menu_bg(self.screen)
                    self.game.show_settings(self.screen)
                    self.game.show_cursor(self.screen)
                    pygame.display.update()

            # This is the main menu loop
            self.game.show_main_bg(self.screen)
            self.game.show_main_menu(self.screen)
            self.game.show_cursor(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

'''import pygame

from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (1000, 1000)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
	display.fill('white')

	board.draw(display)

	pygame.display.update()


running = True
while running:
	mx, my = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				board.handle_click(mx, my)

	if board.is_in_checkmate('black'):
		print('White wins!')
		running = False
	elif board.is_in_checkmate('white'):
		print('Black wins!')
		running = False

	draw(screen)'''


if __name__ == "__main__":
    main = Main()
    main.mainloop()
