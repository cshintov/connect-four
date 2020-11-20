""" The GUI version of the four in a row game """

import sys, math
import pygame

from pprint import pprint

from connect import *

FPS = 20
FramePerSec = pygame.time.Clock()

BLACK = 0, 0, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
YELLOW = 255, 255, 0

SQ_Z = 100
RAD = int(SQ_Z / 2 - 5)

def init(row, col):
    width = col * SQ_Z
    height = (row + 1) * SQ_Z
    size = (width, height)
    pygame.init()
    return pygame.display.set_mode(size)

def create_show_victor(screen):
    myfont = pygame.font.SysFont("monospace", 75)
    def show_victor(player):
        width = COL * SQ_Z
        pygame.draw.rect(screen, BLACK, (0, 0, width, SQ_Z)) 
        msg = f"Player {player} wins !"
        print(msg)
        label = myfont.render(msg, 1, GREEN)
        screen.blit(label, (40, 10))

    return show_victor

def create_draw_board(screen):

    circle_colors = { 0: BLACK, 1: YELLOW, 2: RED }

    def draw_board(board):
        row, col = size(board)
        pprint(board)

        for r in range(row):
            for c in range(col):
                pygame.draw.rect(screen, BLUE, 
                        (c * SQ_Z, r * SQ_Z + SQ_Z, SQ_Z, SQ_Z)) 
                
                color = circle_colors[board[r][c]]
                pygame.draw.circle(screen, color, 
                    (c * SQ_Z + SQ_Z / 2, r * SQ_Z + SQ_Z + SQ_Z / 2), RAD) 

        pygame.display.update()

    return draw_board

def choose_column(player):
    circle_colors = { 0: BLACK, 1: YELLOW, 2: RED }

    col = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            width = COL * SQ_Z
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQ_Z)) 

            x, _ = event.pos
            color = circle_colors[player]
            pygame.draw.circle(screen, color, (x, SQ_Z / 2), RAD) 
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, _ = event.pos
            col = math.floor(x / SQ_Z)
            print(col)

    return col

if __name__ == '__main__':
    ROW, COL = 4, 5
    screen = init(ROW, COL)
    board = create_board(ROW, COL)
    draw_board = create_draw_board(screen)
    draw_board(board)

    show_victor = create_show_victor(screen)

    four_in_a_row = create_four_in_a_row(choose_column, draw_board, show_victor)

    game_over = False
    while not game_over:
        game_over = four_in_a_row(board)
        FramePerSec.tick(FPS)

    pygame.time.wait(3000)

