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

# Load chess board
chess_board = pygame.image.load('assets/chess_board/chess_table_v3.png')
scale_board = pygame.transform.scale(chess_board, (win_width // 2, win_height // 1.3))
board_x = (win_width - scale_board.get_width()) // 2
board_y = (win_height - scale_board.get_height()) // 2

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

# Display text of main menu
font = pygame.font.Font('freesansbold.ttf', 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    screen.blit(scaled_bg, (0, 0))

    # Draw chessboard
    screen.blit(scale_board, (board_x, board_y))

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

    # Keep display updated
    pygame.display.update()
