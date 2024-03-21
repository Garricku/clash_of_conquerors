#!/usr/bin/python3
"""Main - Clash of Conquerors game"""

import pygame
import sys

from const import *
from game import Game
"""Import the constants and the Game class"""


class Main(Game):
    """Main class for game C.O.C."""
    def __init__(self):
        """initialize game and display the screen"""
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Clash Of Conquerors")
        # Load and set the icon
        icon_image = pygame.image.load('assets/icons/coc_icon_bigger.png')
        pygame.display.set_icon(icon_image)
        self.game = Game()

    def mainloop(self):
        """Main game loop"""
        while True:
            if self.game.play == True:
                while self.game.play == True:
                    self.game.show_game_bg(self.screen)
                    self.game.show_chessboard(self.screen)
                    self.game.show_profiles(self.screen)
                    self.game.show_menu_button(self.screen)
                    self.game.show_timer(self.screen)
                    
                    if self.game.menu_state == True:
                        self.game.show_game_menu(self.screen)
                        self.game.show_cursor(self.screen)

                    self.game.show_cursor(self.screen)

                    pygame.display.update()

            elif self.game.get_opt() == True:
                pass

            elif self.game.get_help() == True:
                pass

            else:
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