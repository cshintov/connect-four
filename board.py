""" 
Represents a four-in-a-row board.

Uses a grid (2 X 2 matrix) to represent the board.
"""


def create_board(rows, colns):
    """ Creates a rows X colns grid """
    return [[0 for c in range(colns)] 
                for r in range(rows) ]

def size(board):
    """ Calculate the size (rows, cols) of the board """
    try:
        return (len(board), len(board[0])) 
    except:
        return (0, 0)

def up(b, x, y):
    """ Returns the coordinates of the above cell in the grid """
    x1, y1 = x - 1, y
    if x1 < 0:
        return None
    return (x1, y1)

def down(b, x, y):
    """ Returns the coordinates of the below cell in the grid """
    r, c = size(b)
    x1, y1 = x + 1, y
    if not x1 < r:
        return None
    return (x1, y1)

def left(b, x, y):
    """ Returns the coordinates of the left cell in the grid """
    x1, y1 = x, y - 1
    if y1 < 0:
        return None
    return (x1, y1)

def right(b, x, y):
    """ Returns the coordinates of the right cell in the grid """
    r, c = size(b)
    x1, y1 = x, y + 1
    if not y1 < c:
        return None
    return (x1, y1)

def diagonals(d1, d2):
    """ A higher order function that accepts two directions d1 and d2
    and returns the coordinates of the cell reached after moving
    first d1 and then d2 """

    def inner(b, x, y):
        coord = d1(b, x, y)
        return None if not coord else d2(b, *coord)

    return inner

# The below functions created using 'diagonals' can be used
# to get the coordinates of the adjacent cells of a cell when
# moved diagonally

left_up = diagonals(left, up)
left_down = diagonals(left, down)
right_up = diagonals(right, up)
right_down = diagonals(right, down)

def winning_config(b, x, y, p, move=right):
    """ Generates a winning configuration using the given direction """
    r, k = x, y
    for i in range(4):
        b[r][k] = p
        try:
            r, k = move(b, r, k)
        except TypeError:
            break
    return b


if __name__ == "__main__":
    ROW, COL = 6, 7

    b1 = create_board(ROW, COL) 
    c1 = winning_config(b1, 0, 0, 1)
    #c2 = winning_config(b1, 0, 0, 1, down)
    #c3 = winning_config(b1, 3, 0, 1)
    c4 = winning_config(b1, 3, 3, 1, right_down)

    p = 1
    score = p_won(c4, 5, 2, p)
    if score:
        print(f'{p} Won!')
    else:
        print(f'{p} did  not Win')

    print(c4)
