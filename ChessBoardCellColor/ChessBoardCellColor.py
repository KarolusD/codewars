print('hello')
# Given two cells on the standard chess board, determine whether they have the same color or not.


def chess_board_cell_color(cell1, cell2):
    col1, row1 = list(cell1)
    col2, row2 = list(cell2)

    ASCII = 64

    sum1 = ord(col1) - ASCII + int(row1)
    sum2 = ord(col2) - ASCII + int(row2)

    return sum1 % 2 == sum2 % 2


tests = [
    # [[cell1, cell2], expected],
    [["A1", "C3"], True],
    [["A1", "H3"], False],
    [["A1", "A2"], False],
]


def f():
    for inp in tests:
        print(chess_board_cell_color(inp[0][0], inp[0][1]), inp[1])


f()
