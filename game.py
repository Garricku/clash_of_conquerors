#!/usr/bin/python3
"""Clash of Conquerors - Chess Game main game GUI"""

import pygame
import sys
"""These are imported modules used for game creation"""


# Window size
win_width = 1280
win_height = 720

# Load custom mouse cursor
cursor_image = pygame.image.load('assets/cursors/custom_cursor.png')

# Load and set the icon
icon_image = pygame.image.load('assets/icons/coc_icon_bigger.png')
pygame.display.set_icon(icon_image)

# Load background
bg_img = pygame.image.load('assets/backgrounds/background_0.png')
scaled_bg = pygame.transform.scale(bg_img, (win_width, win_height))

# Load buttons and bars
menu_button = pygame.image.load('assets/buttons/menu_button_small.png')
bar_x = (win_width - menu_button.get_width()) - 40
bar_y = (win_height - menu_button.get_height()) // 9

# Players profiles
opponent_img = pygame.image.load('assets/borders/opponent_img.png')
player_img = pygame.image.load('assets/borders/player_img.png')
player_x = (win_width - player_img.get_width()) + 30
player_y = (win_height - player_img.get_height()) + 70

opponent_name_tag = pygame.image.load('assets/borders/rectangle_border.png')
scale_tag_opp = pygame.transform.scale(opponent_name_tag, (350, 60))
player_name_tag = pygame.image.load('assets/borders/rectangle_border.png')
scale_tag_play = pygame.transform.scale(player_name_tag, (350, 60))
dag_x = (win_width - scale_tag_play.get_width()) - 130
dag_y = (win_height - scale_tag_play.get_height())

op_profile_img = pygame.image.load('assets/profile_pictures/profile_default.png')
scale_op_pic = pygame.transform.scale(op_profile_img, (150, 150))
pl_profile_img = pygame.image.load('assets/profile_pictures/profile_default_2.png')
scale_ppic = pygame.transform.scale(pl_profile_img, (150, 150))
ppic_x = (win_width - scale_ppic.get_width()) - 20
ppic_y = (win_height - scale_ppic.get_height())

# Timer
timer_border = pygame.image.load('assets/borders/rectangle_border.png')
scale_timer = pygame.transform.scale(timer_border, (180, 140))
timer_y = (win_height - scale_timer.get_height()) -80

# Chess pieces
w_king = pygame.image.load('assets/chess_pieces/white_king.png')
scale_w_king = pygame.transform.scale(w_king, (85, 70))
col_4 = 248
row_1 = 404

w_pawn = pygame.image.load('assets/chess_pieces/white_pawn.png')
scale_w_pawn = pygame.transform.scale(w_pawn, (85, 70))
col_3 = 220
row_3 = 404

pygame.init()

# Set game window
screen = pygame.display.set_mode((win_width, win_height), pygame.FULLSCREEN)
pygame.display.set_caption("Clash Of Conquerors")
pygame.mouse.set_visible(False)  # Hide default cursor

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
            pygame.draw.rect(screen, 'white', [850 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'white', [950 - (column * 200), row * 100, 100, 100])

def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 272, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 260, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 272, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 260, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        '''if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)'''
        if piece == 'queen':
            moves_list = check_queen(location, turn)
        '''elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)'''
    return all_moves_list

# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


#black_options = check_options(black_pieces, black_locations, 'black')
#white_options = check_options(white_pieces, white_locations, 'white')
while True:
    draw_pieces()
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

    # Draw background
    screen.blit(scaled_bg, (0, 0))

    # Draw chessboard

    # Draw chess pieces
    screen.blit(scale_w_pawn, (row_3, col_3))
    screen.blit(scale_w_king, (row_1, col_4))

    # Player and opponent profiles
    screen.blit(scale_op_pic, (20, -20))
    screen.blit(scale_ppic, (ppic_x, ppic_y))
    screen.blit(scale_tag_opp, (130, 7))
    screen.blit(scale_tag_play, (dag_x, dag_y))
    screen.blit(opponent_img, (-30, -70))
    screen.blit(player_img, (player_x, player_y))

    # Draw menu button and timer
    screen.blit(menu_button, (bar_x, bar_y))
    screen.blit(scale_timer, (45, timer_y))

    # Draw custom cursor
    cursor_rect = cursor_image.get_rect(center=pygame.mouse.get_pos())
    screen.blit(cursor_image, cursor_rect)

    chess_board()

    # Keep display updated
    pygame.display.update()