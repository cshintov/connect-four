""" 
The GUI version of the four in a row game.

Reuses the connect module for game logic.
The game rendering is handled by pygame library.
"""

import pygame
import sys, math
from pprint import pprint

from connect import *

pygame.init

FPS = 20
FramePerSec = pygame.time.Clock()

BLACK = 0, 0, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
YELLOW = 255, 255, 0

SQUARE_SIZE = 100
RAD = int(SQUARE_SIZE / 2 - 5)


def init(row, col):
    """Initialize the pygame screen.
    The size of the screen is calculated from row and col
    and SQUARE_SIZE
    """
    width = col * SQUARE_SIZE
    height = (row + 1) * SQUARE_SIZE
    size = (width, height)
    pygame.init()
    return pygame.display.set_mode(size)


def create_show_victor(screen):
    """ Returns a function that displays the victor on the screen """

    myfont = pygame.font.SysFont("monospace", 75)

    def show_victor(player):
        width = COL * SQUARE_SIZE
        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
        msg = f"Player {player} wins !"
        print(msg)
        label = myfont.render(msg, 1, GREEN)
        screen.blit(label, (40, 10))

    return show_victor


def create_draw_board(screen):
    """ Returns a function that draws the game board on the pygame screen """

    circle_colors = {0: BLACK, 1: YELLOW, 2: RED}

    def draw_board(board):
        row, col = size(board)
        print(board)

        for r in range(row):
            for c in range(col):
                pygame.draw.rect(
                    screen,
                    BLUE,
                    (
                        c * SQUARE_SIZE,
                        r * SQUARE_SIZE + SQUARE_SIZE,
                        SQUARE_SIZE,
                        SQUARE_SIZE,
                    ),
                )

                color = circle_colors[board[r][c]]
                pygame.draw.circle(
                    screen,
                    color,
                    (
                        c * SQUARE_SIZE + SQUARE_SIZE / 2,
                        r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2,
                    ),
                    RAD,
                )

        pygame.display.update()

    return draw_board


def choose_column(player):
    circle_colors = {0: BLACK, 1: YELLOW, 2: RED}

    col = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Follow the mouse pointer and draw a circle of the current player
        if event.type == pygame.MOUSEMOTION:
            width = COL * SQUARE_SIZE
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))

            x, _ = event.pos
            color = circle_colors[player]
            pygame.draw.circle(screen, color, (x, SQUARE_SIZE / 2), RAD)
            pygame.display.update()

        # Choose column in case of a mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, _ = event.pos
            col = math.floor(x / SQUARE_SIZE)
            print(col)

    return col


if __name__ == "__main__":
    ROW, COL = 6, 7
    screen = init(ROW, COL)
    board = create_board(ROW, COL)
    draw_board = create_draw_board(screen)
    show_victor = create_show_victor(screen)
    four_in_a_row = create_four_in_a_row(choose_column, draw_board, show_victor)

    game_over = False
    draw_board(board)

    while not game_over:
        game_over = four_in_a_row(board)
        FramePerSec.tick(FPS)

    pygame.time.wait(3000)
