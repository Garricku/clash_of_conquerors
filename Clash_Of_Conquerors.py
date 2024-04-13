#!/usr/bin/python3
"""Main - Clash of Conquerors game"""

import pygame
import sys

from const import *
from game import Game
from chess import Chess
from board import Board
"""Imported modules"""


class Main(Game):
    """Main class for game C.O.C."""
    
    def __init__(self):
        """initialize game and display the screen"""
        pygame.init()
        self.game = Game()
        self.chess = Chess()
        self.screen = pygame.display.set_mode((self.game.WIN_WIDTH, self.game.WIN_HEIGHT))
        pygame.display.set_caption("Clash Of Conquerors")
        # Load and set the icon
        icon_image = pygame.image.load('assets/icons/coc_icon_bigger.png')
        pygame.display.set_icon(icon_image)
        self.board = Board()
    
    def draw(self):
        """Draws the white blocks for the chess board"""
        self.screen.fill('white')

    def mainloop(self):
        """Main game loop"""
        while True:
            while self.game.opt: # Setting menu loop starts here
                self.game.show_menu_bg(self.screen)
                self.game.show_settings(self.screen)
                self.game.show_cursor(self.screen)
                pygame.display.update()

            while self.game.help: # Tutorial loop
                self.game.show_tour_bg(self.screen)
                self.game.show_tutorial(self.screen)
                self.game.show_cursor(self.screen)
                pygame.display.update()

            while self.game.play: # Chess game loop starts here
                mx, my = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game.play = False
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.board.handle_click(mx, my)
                            if self.board.is_in_checkmate('black'):
                                print('White wins!')
                                self.game.play = False
                            elif self.board.is_in_checkmate('white'):
                                print('Black wins!')
                                self.game.play = False
                            elif self.game.rect_menu_button.collidepoint(event.pos):
                                self.game.set_menu_state(True)

                self.game.show_game_bg(self.screen)
                self.board.draw(self.screen)
                self.game.show_profiles(self.screen)
                self.game.show_menu_button(self.screen)
                self.game.show_cursor(self.screen)
                
                pygame.display.update()

                while self.game.menu_state: # This is in the chess game loop
                    self.game.show_menu_bg(self.screen)
                    self.game.show_game_menu(self.screen)
                    self.game.show_cursor(self.screen)
                    pygame.display.update()

                while self.game.opt: # This is in the menu loop of chess game loop
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


if __name__ == "__main__":
    main = Main()
    main.mainloop()
