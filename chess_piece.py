#!/usr/bin/python3
"""Chess Piece module"""

import pygame


class ChessPiece:
    """The chess piece class"""
    def __init__(self, image_path, x, y):
        """Initialize the chess piece"""
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.killed = False

    def show_piece(self, surface, piece, x, y):
        """Display the chess Piece on the rectangle"""
        surface.blit(piece, (x, y))

    def kill_piece(self):
        """Kill a piece and remove it from the field"""
        self.killed = True

    def move_piece(self, x, y):
        """Moves a piece by changing it's x & y blit point """
        self.rect.x = x
        self.rect.y = y

    def check_collision(self, other_piece):
        """Check if the point moved to is occupied by another rectangle"""
        return self.rect.colliderect(other_piece.rect) # Returns true or false
