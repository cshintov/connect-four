import numpy as np

from board import *

ROW, COL = 6, 7

def create_board():
    board = np.zeros((ROW, COL))
    return board

def is_valid_location(board, col):
    return board[0][col] == 0

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def get_next_open_row(board, col):
    for r in range(ROW - 1, -1, -1):
        if board[r][col] == 0:
            return r

def winning_move(b, x, y, p):
    """ Checks whether p won by playing (x, y) """

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

def read_int():
    try:
        int(input('Player 1: '))
    except ValueError:
        return 0

def main():
    board = create_board()
    P1, P2 = 1, 2

    player = P1

    game_over = False

    while not game_over:
        try:
            col = int(input(f'Player {player}: '))
        except ValueError:
            continue

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, player)
        else:
            print(f'{col + 1} th Column Full!')
            print(board)
            continue

        if winning_move(board, row, col, player):
            print(f'Game Over! Player {player} wins!')
            game_over = True

        player = P1 if player == P2 else P2

        print(board)

if __name__ == '__main__':
    main()
    board = create_board()
