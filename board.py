import numpy as np

ROW, COL = 6, 7

def create_board():
    board = np.zeros((ROW, COL))
    return board

def size(board):
    return (len(board), len(board[0])) if len(board) > 0 else (0, 0)

def up(b, x, y):
    x1, y1 = x - 1, y
    if x1 < 0:
        return None
    return (x1, y1)

def down(b, x, y):
    r, c = size(b)
    x1, y1 = x + 1, y
    if not x1 < r:
        return None
    return (x1, y1)

def left(b, x, y):
    x1, y1 = x, y - 1
    if y1 < 0:
        return None
    return (x1, y1)

def right(b, x, y):
    r, c = size(b)
    x1, y1 = x, y + 1
    if not y1 < c:
        return None
    return (x1, y1)

def diagonals(d1, d2):

    def inner(b, x, y):
        coord = d1(b, x, y)
        return None if not coord else d2(b, *coord)

    return inner

def winning_config(b, x, y, p, move=right):
    r, k = x, y
    for i in range(4):
        b[r][k] = p
        try:
            r, k = move(b, r, k)
        except TypeError:
            break
    return b

left_up = diagonals(left, up)
left_down = diagonals(left, down)
right_up = diagonals(right, up)
right_down = diagonals(right, down)

b1 = create_board() 

c1 = winning_config(b1, 0, 0, 1)
#c2 = winning_config(b1, 0, 0, 1, down)
#c3 = winning_config(b1, 3, 0, 1)
c4 = winning_config(b1, 3, 3, 1, right_down)

if __name__ == "__main__":
    p = 1
    score = p_won(c4, 5, 2, p)
    if score:
        print(f'{p} Won!')
    else:
        print(f'{p} didn not Win')

    print(c4)
