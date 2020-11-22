""" 
This modules contains the main game logic as well as
the command line game play of the four-in-a-row game.
"""

import sys
from pprint import pprint

from board import *


def is_valid_location(board, col):
    return board[0][col] == 0


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def get_next_open_row(board, col):
    row, _ = size(board)
    for r in range(row - 1, -1, -1):
        if board[r][col] == 0:
            return r


def winning_move(b, x, y, p):
    """ Checks whether p won by playing at cell (x, y)"""

    def count(i, j, direction, score=0, turn=1):
        nxt_cell = direction(b, i, j)

        if not nxt_cell or turn == 4:
            return score

        x1, y1 = nxt_cell

        if b[x1][y1] == p:
            return count(x1, y1, direction, score + 1, turn + 1)

        return score

    if b[x][y] == p:
        horiz = count(x, y, left) + 1 + count(x, y, right)
        vert = count(x, y, up) + 1 + count(x, y, down)
        fwd_diag = count(x, y, left_down) + 1 + count(x, y, right_up)
        bwd_diag = count(x, y, left_up) + 1 + count(x, y, right_down)

        score = max(horiz, vert, fwd_diag, bwd_diag)
    else:
        score = 0

    return score >= 4


def read_int(player):
    try:
        return int(input(f"Player {player}: "))
    except ValueError:
        return 0
    except KeyboardInterrupt:
        print("\nUser chose to quit!")
        sys.exit()


def print_victor(player):
    print(f"Game Over! Player {player} wins!")


def create_four_in_a_row(
    choose_column=read_int, refresh=print, show_victor=print_victor
):
    """
    choose_column: how the user chooses the column to play.
    refresh: how the board is rendered every time a play is made.
    show_victor: how the victor is shown after the game.
    """

    P1, P2 = 1, 2
    player = P1
    game_over = False

    def four_in_a_row(board):
        nonlocal player, game_over

        # Choose column to play.
        # In case column is not chosen properly continue with the game.
        try:
            col = choose_column(player)
        except Exception as err:
            print(err)
            print("Invalid input!")
            return not game_over

        if col is None:
            return game_over

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, player)
        else:
            print(f"{col + 1} th Column Full!")
            return game_over

        if winning_move(board, row, col, player):
            show_victor(player)
            game_over = True

        refresh(board)
        player = P1 if player == P2 else P2

        return game_over

    return four_in_a_row


if __name__ == "__main__":
    ROW, COL = 4, 5
    board = create_board(ROW, COL)
    print(board)
    four_in_a_row = create_four_in_a_row(read_int, print, print_victor)
    game_over = False

    while not game_over:
        game_over = four_in_a_row(board)
