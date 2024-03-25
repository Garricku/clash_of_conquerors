#!/usr/bin/python3
"""Main - Clash of Conquerors game"""

import pygame
import sys

from const import *
from game import Game
from chess import Chess
#from chess_piece import ChessPiece
"""Import the constants and the Game class"""


class Main(Game):
    """Main class for game C.O.C."""
    def __init__(self):
        """initialize game and display the screen"""
        pygame.init()
        self.game = Game()
        self.chess = Chess()
        #self.piece = ChessPiece()
        self.screen = pygame.display.set_mode((self.game.WIN_WIDTH, self.game.WIN_HEIGHT))
        pygame.display.set_caption("Clash Of Conquerors")
        # Load and set the icon
        icon_image = pygame.image.load('assets/icons/coc_icon_bigger.png')
        pygame.display.set_icon(icon_image)

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
                self.chess.chess_board(self.screen)
                self.chess.draw_pieces(self.screen)
                self.game.show_profiles(self.screen)
                self.game.show_menu_button(self.screen)
                self.game.show_timer(self.screen)
                self.game.show_cursor(self.screen)
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
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x_coord = event.pos[0] // 100
                    y_coord = event.pos[1] // 100
                    click_coords = (x_coord, y_coord)
                    if self.turn_step <= 1:
                        if click_coords in self.white_locations:
                            selection = self.white_locations.index(click_coords)
                            if self.turn_step == 0:
                                self.turn_step = 1
                        if click_coords in self.valid_moves and selection != 100:
                            self.white_location[selection] = click_coords
                            if click_coords in self.black_location:
                                black_piece = self.black_location.index(click_coords)
                                self.captured_pieces_white.append(self.black_pieces[black_piece])
                                self.black_pieces.pop(black_piece)
                                self.black_locations.pop(black_piece)
                            black_options = self.check_options()
                            white_options = self.check_options()
                            turn_step = 2
                            selection = 100
                            valid_moves = []
                    
                    if self.turn_step > 1:
                        if click_coords in self.black_locations:
                            selection = self.black_locations.index(click_coords)
                            if self.turn_step == 2:
                                self.turn_step == 3
                        if click_coords in self.valid_moves and selection != 100:
                            self.black_location[selection] = click_coords
                            if click_coords in self.white_location:
                                white_piece = self.white_location.index(click_coords)
                                self.captured_pieces_black.append(self.white_pieces[white_piece])
                                self.white_pieces.pop(white_piece)
                                self.white_locations.pop(white_piece)
                            black_options = self.check_options()
                            white_options = self.check_options()
                            turn_step = 0
                            selection = 80
                            valid_moves = []

            # This is the main menu loop
            self.game.show_main_bg(self.screen)
            self.game.show_main_menu(self.screen)
            self.game.show_cursor(self.screen)

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.mainloop()
