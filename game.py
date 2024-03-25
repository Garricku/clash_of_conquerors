#!/usr/bin/python3
"""This is the chess game screen module"""

import pygame
import sys

from const import *
"""Imports the constants"""


class Game():
    """The class for the chess game screen"""
    def __init__(self):
        """Initialize the attributes"""
        self.play = False
        self.opt = False
        self.help = False
        self.menu_state = False
        screen_info = pygame.display.Info()
        self.WIN_WIDTH = screen_info.current_w
        self.WIN_HEIGHT = screen_info.current_h

    def get_win_width(self):
        """Returns the window width"""
        return self.WIN_WIDTH

    def get_win_height(self):
        """Returns the window height"""
        return self.WIN_HEIGHT

    def get_play(self):
        """Returns the play attribute bool"""
        return self.play

    def get_opt(self):
        """Returns the opt attribute bool"""
        return self.opt

    def get_help(self):
        """Returns the help attribute bool"""
        return self.help

    def get_menu_state(self):
        """Returns the state of game menu"""
        return self.menu_state

    def set_play(self, state):
        """Sets the play attribute bool"""
        self.play = state

    def set_opt(self, state):
        """Sets the opt attribute bool"""
        self.opt = state

<<<<<<< HEAD
pygame.init()
=======
    def set_help(self, state):
        """Sets the help attribute bool"""
        self.help = state

    def set_menu_state(self, state):
        """Sets the state of the in game menu"""
        self.menu_state = state

    def show_main_bg(self, surface):
        """Displays the background for the main menu"""
        bg_img = pygame.image.load('assets/title_screens/title_coc_2.png')
        scaled_bg = pygame.transform.scale(bg_img, (self.WIN_WIDTH, self.WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))
>>>>>>> origin/master

    def show_main_menu(self, surface):
        """Displays the main menu"""
        # Load the main menu
        main_menu = pygame.image.load('assets/menus/menu_list.png')
        main_menu.set_alpha(240)
        scaled_main_menu = pygame.transform.scale(main_menu, (self.WIN_WIDTH // 2.3, self.WIN_HEIGHT // 1.2))
        menu_x = (self.WIN_WIDTH - scaled_main_menu.get_width()) // 2
        menu_y = (self.WIN_HEIGHT - scaled_main_menu.get_height()) // 2
        # This is the underline for menu selection
        underline = pygame.image.load('assets/menus/underline.png')
        underline.set_alpha(0)
        underline_help = pygame.image.load('assets/menus/underline.png')
        underline_help.set_alpha(0)
        underline_exit = pygame.image.load('assets/menus/underline.png')
        underline_exit.set_alpha(0)
        underline_opt = pygame.image.load('assets/menus/underline.png')
        underline_opt.set_alpha(0)
        # Display text of main menu
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('PLAY', True, (60, 60, 60), None)
        textRect = text.get_rect()
        textRect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2)

<<<<<<< HEAD
#setup game variables
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
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False

# Display text of main menu
font = pygame.font.Font('freesansbold.ttf', 32)

def chess_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'white', [850 - (column * 150), 65 + (row * 75), 75, 75])
        else:
            pygame.draw.rect(screen, 'white', [950 - (column * 160), 65 + (row * 75), 75, 75])
        if row % 2 == 1:
            pygame.draw.rect(screen, 'black', [850 - (column * 150), 65 + (row * 75), 75, 75])
        else:
            pygame.draw.rect(screen, 'black', [950 - (column * 160), 65 + (row * 75), 75, 75])

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'purple', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        if piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# check rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
=======
        menu_opt = font.render('SETTINGS', True, (60, 60, 60), None)
        opt_rect = menu_opt.get_rect()
        opt_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 50)

        menu_help = font.render('TUTORIAL', True, (60, 60, 60), None)
        help_rect = menu_help.get_rect()
        help_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 100)
>>>>>>> origin/master

        menu_exit = font.render('EXIT', True, (60, 60, 60), None)
        exit_rect = menu_exit.get_rect()
        exit_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 150)

<<<<<<< HEAD
    # Player and opponent profiles
    screen.blit(scale_op_pic, (20, -20))
    screen.blit(scale_ppic, (ppic_x, ppic_y))
    screen.blit(scale_tag_opp, (130, 7))
    screen.blit(scale_tag_play, (dag_x, dag_y))
    screen.blit(opponent_img, (-30, -70))
    screen.blit(player_img, (player_x, player_y))
=======
        play_line = text.get_rect()
        play_line.center = (self.WIN_WIDTH // 2 - 44, self.WIN_HEIGHT // 2 + 25)
        opt_line = menu_opt.get_rect()
        opt_line.center = (self.WIN_WIDTH // 2 - 2, self.WIN_HEIGHT // 2 + 75)
        help_line = menu_opt.get_rect()
        help_line.center = (self.WIN_WIDTH // 2 - 2, self.WIN_HEIGHT // 2 + 125)
        exit_line = menu_opt.get_rect()
        exit_line.center = (self.WIN_WIDTH // 2 - 4, self.WIN_HEIGHT // 2 + 175)

        surface.blit(scaled_main_menu, (menu_x, menu_y))
        # Draw the text
        surface.blit(text, textRect)
        surface.blit(menu_opt, opt_rect)
        surface.blit(menu_help, help_rect)
        surface.blit(menu_exit, exit_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    # Button clicked!
                    pygame.quit()
                    sys.exit()
>>>>>>> origin/master

                elif textRect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_play(True)

<<<<<<< HEAD
    # Draw custom cursor
    chess_board()
    draw_pieces()

    cursor_rect = cursor_image.get_rect(center=pygame.mouse.get_pos())
    screen.blit(cursor_image, cursor_rect)
    # Keep display updated
    pygame.display.update()
=======
                elif opt_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_opt(True)

                elif help_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_help(True)

        # Check if the mouse is hovering over the text rectangle
        if textRect.collidepoint(pygame.mouse.get_pos()):
            # Make underline visible
            underline.set_alpha(255)
            surface.blit(underline, play_line)
        else:
            # Make underline invisible
            underline.set_alpha(0)
            surface.blit(underline, play_line)

        if opt_rect.collidepoint(pygame.mouse.get_pos()):
            underline_opt.set_alpha(255)
            surface.blit(underline_opt, opt_line)
        else:
            underline_opt.set_alpha(0)
            surface.blit(underline_opt, opt_line)

        if help_rect.collidepoint(pygame.mouse.get_pos()):
            underline_help.set_alpha(255)
            surface.blit(underline_help, help_line)
        else:
            underline_help.set_alpha(0)
            surface.blit(underline_help, help_line)

        if exit_rect.collidepoint(pygame.mouse.get_pos()):
            underline_exit.set_alpha(255)
            surface.blit(underline_exit, exit_line)
        else:
            underline_exit.set_alpha(0)
            surface.blit(underline_exit, exit_line)

    def show_cursor(self, surface):
        """Displays the custom cursor"""
        # Load custom mouse cursor
        cursor_image = pygame.image.load('assets/cursors/custom_cursor.png')
        # Hide default cursor
        pygame.mouse.set_visible(False)
        # Draw custom cursor
        cursor_rect = cursor_image.get_rect(center=pygame.mouse.get_pos())
        surface.blit(cursor_image, cursor_rect)

    def show_menu_bg(self, surface):
        """Displays the background for menus"""
        bg_img = pygame.image.load('assets/title_screens/title_coc_1.png')
        scaled_bg = pygame.transform.scale(bg_img, (self.WIN_WIDTH, self.WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))

    def fade_out_fade_in(self, surface):
        """Fades out to black for smoother transitions"""
        color = (0, 0, 0) # Black
        visibility = 0 # Invisible
        while visibility <= 255:
            surface.fill(color, (visibility))
            visibility += 5 # Increase visibility till fully black
        while visibility >= 0:
            surface.fill(color, (visibility))
            visibility -= 5 # Decrease the visibility till no black

    def show_settings(self, surface):
        """Displays the settings menu"""
        font = pygame.font.Font('freesansbold.ttf', 32)
        settings_display = pygame.image.load('assets/borders/timer_border_2.png')
        scaled_setts = pygame.transform.scale(settings_display, (self.WIN_WIDTH, self.WIN_HEIGHT - 70))
        underline_back = pygame.image.load('assets/menus/underline.png')
        underline_back.set_alpha(0)
        menu_back = font.render('RETURN', True, (160, 160, 160), None)
        back_rect = menu_back.get_rect()
        back_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 210)
        back_line = menu_back.get_rect()
        back_line.center = (self.WIN_WIDTH // 2 - 19, self.WIN_HEIGHT // 2 + 235)

        surface.blit(scaled_setts, (0, 50))
        surface.blit(menu_back, back_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_opt(False)

        if back_rect.collidepoint(pygame.mouse.get_pos()):
            underline_back.set_alpha(255)
            surface.blit(underline_back, back_line)
        else:
            underline_back.set_alpha(0)
            surface.blit(underline_back, back_line)

    def show_tutorial(self, surface):
        """Display the how to play screen"""
        font = pygame.font.Font('freesansbold.ttf', 32)
        settings_display = pygame.image.load('assets/borders/timer_border_2.png')
        scaled_setts = pygame.transform.scale(settings_display, (self.WIN_WIDTH, self.WIN_HEIGHT - 70))
        underline_back = pygame.image.load('assets/menus/underline.png')
        underline_back.set_alpha(0)
        menu_back = font.render("RETURN", True, (160, 160, 160), None)
        back_rect = menu_back.get_rect()
        back_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 210)
        back_line = menu_back.get_rect()
        back_line.center = (self.WIN_WIDTH // 2 - 19, self.WIN_HEIGHT // 2 + 235)

        surface.blit(scaled_setts, (0, 50))
        surface.blit(menu_back, back_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_help(False)

        if back_rect.collidepoint(pygame.mouse.get_pos()):
            underline_back.set_alpha(255)
            surface.blit(underline_back, back_line)
        else:
            underline_back.set_alpha(0)
            surface.blit(underline_back, back_line)

    def show_game_bg(self, surface):
        """
        Displays the in-game background
        Loads the background image
        Resizes it then draws it on the screen
        """
        bg_img = pygame.image.load('assets/backgrounds/background_0.png')
        scaled_bg = pygame.transform.scale(bg_img, (self.WIN_WIDTH, self.WIN_HEIGHT))
        surface.blit(scaled_bg, (0, 0))

    def show_profiles(self, surface):
        """Displays player and opponent profiles"""
        opponent_img = pygame.image.load('assets/borders/opponent_img.png')
        player_img = pygame.image.load('assets/borders/player_img.png')
        player_x = (self.WIN_WIDTH - player_img.get_width()) + 30
        player_y = (self.WIN_HEIGHT - player_img.get_height()) + 70

        opponent_name_tag = pygame.image.load('assets/borders/rectangle_border.png')
        scale_tag_opp = pygame.transform.scale(opponent_name_tag, (350, 60))
        player_name_tag = pygame.image.load('assets/borders/rectangle_border.png')
        scale_tag_play = pygame.transform.scale(player_name_tag, (350, 60))
        dag_x = (self.WIN_WIDTH - scale_tag_play.get_width()) - 130
        dag_y = (self.WIN_HEIGHT - scale_tag_play.get_height())

        op_profile_img = pygame.image.load('assets/profile_pictures/profile_default.png')
        scale_op_pic = pygame.transform.scale(op_profile_img, (150, 150))
        pl_profile_img = pygame.image.load('assets/profile_pictures/profile_default_2.png')
        scale_ppic = pygame.transform.scale(pl_profile_img, (150, 150))
        ppic_x = (self.WIN_WIDTH - scale_ppic.get_width()) - 20
        ppic_y = (self.WIN_HEIGHT - scale_ppic.get_height())

        surface.blit(scale_op_pic, (20, -20))
        surface.blit(scale_ppic, (ppic_x, ppic_y))
        surface.blit(scale_tag_opp, (130, 7))
        surface.blit(scale_tag_play, (dag_x, dag_y))
        surface.blit(opponent_img, (-30, -70))
        surface.blit(player_img, (player_x, player_y))

    def show_timer(self, surface):
        """Displays the timer"""
        timer_border = pygame.image.load('assets/borders/rectangle_border.png')
        scale_timer = pygame.transform.scale(timer_border, (180, 140))
        timer_y = (self.WIN_HEIGHT - scale_timer.get_height()) -80
        surface.blit(scale_timer, (45, timer_y))

    def show_menu_button(self, surface):
        """Draw menu button and timer"""
        menu_button = pygame.image.load('assets/buttons/menu_button_small.png')
        rect_menu_button = menu_button.get_rect()
        rect_menu_button.center = (self.WIN_WIDTH - 100, 100)
        surface.blit(menu_button, rect_menu_button)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_menu_button.collidepoint(event.pos):
                    self.set_menu_state(True)

    def show_game_menu(self, surface):
        """Displays the in game menu"""
        game_menu = pygame.image.load('assets/menus/coc_menu.png')
        scaled_game_menu = pygame.transform.scale(game_menu, (self.WIN_WIDTH // 3, self.WIN_HEIGHT // 1.5))
        game_menu_x = (self.WIN_WIDTH - scaled_game_menu.get_width()) // 2
        game_menu_y = (self.WIN_HEIGHT - scaled_game_menu.get_height()) // 2

        # This is the underline for menu selection
        underline_surrender = pygame.image.load('assets/menus/underline.png')
        underline_surrender.set_alpha(0)
        underline_continue = pygame.image.load('assets/menus/underline.png')
        underline_continue.set_alpha(0)
        underline_setts = pygame.image.load('assets/menus/underline.png')
        underline_setts.set_alpha(0)

        # Display text of main menu
        font = pygame.font.Font('freesansbold.ttf', 32)
        menu_setts = font.render('Settings', True, (220, 50, 50), None)
        setts_rect = menu_setts.get_rect()
        setts_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 50)

        menu_surrender = font.render('Surrender', True, (220, 50, 50), None)
        surrender_rect = menu_surrender.get_rect()
        surrender_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 100)

        menu_continue = font.render('Continue', True, (220, 50, 50), None)
        continue_rect = menu_continue.get_rect()
        continue_rect.center = (self.WIN_WIDTH // 2, self.WIN_HEIGHT // 2 + 150)

        setts_line = menu_setts.get_rect()
        setts_line.center = (self.WIN_WIDTH // 2 - 15, self.WIN_HEIGHT // 2 + 75)
        surrender_line = menu_setts.get_rect()
        surrender_line.center = (self.WIN_WIDTH // 2 - 15, self.WIN_HEIGHT // 2 + 125)
        continue_line = menu_setts.get_rect()
        continue_line.center = (self.WIN_WIDTH // 2 - 15, self.WIN_HEIGHT // 2 + 175)

        surface.blit(scaled_game_menu, (game_menu_x, game_menu_y))

        # Draw the text
        surface.blit(menu_setts, setts_rect)
        surface.blit(menu_surrender, surrender_rect)
        surface.blit(menu_continue, continue_rect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_menu_state(False)

                if setts_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_menu_state(False)
                    self.set_opt(True)

                if surrender_rect.collidepoint(event.pos):
                    # Button clicked!
                    self.set_menu_state(False)
                    self.set_play(False)

        # Check if the mouse is hovering over the text rectangle
        if setts_rect.collidepoint(pygame.mouse.get_pos()):
            underline_setts.set_alpha(255)
            surface.blit(underline_setts, setts_line)
        else:
            underline_setts.set_alpha(0)
            surface.blit(underline_setts, setts_line)

        if surrender_rect.collidepoint(pygame.mouse.get_pos()):
            underline_surrender.set_alpha(255)
            surface.blit(underline_surrender, surrender_line)
        else:
            underline_surrender.set_alpha(0)
            surface.blit(underline_surrender, surrender_line)

        if continue_rect.collidepoint(pygame.mouse.get_pos()):
            underline_continue.set_alpha(255)
            surface.blit(underline_continue, continue_line)
        else:
            underline_continue.set_alpha(0)
            surface.blit(underline_continue, continue_line)
>>>>>>> origin/master
