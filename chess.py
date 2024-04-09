#!/usr/bin/python3
"""The chess game logic module Chess class"""

import pygame

from const import *
"""Import the constants"""


class Chess():
    """Chess class inherits from Game"""
    def __init__(self):
        """Initialize the chess game logic base variables"""
        self.color_1 = (255, 255, 255)
        self.color_2 = (0, 0, 0)

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
