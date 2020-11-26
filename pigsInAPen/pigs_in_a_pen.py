print('hello, friend')
# n - horizontal line (poziom)
# n + board           n - board
# n + board + 1       n - board - 1
# n + 2*board + 1     n - 2*board - 1

# n - vertical line (pion)
# n + 1               n - 1
# n - board           n + board
# n + board + 1       n - board - 1

# board 2x2
# 1-2 horizontal line
# 3-5 vertical line
# 6-7 horizontal line
# 8-10 vertical line

# board 2x2
# [3,4,6]

# all_lines_in_board = board * (board + 4)


def lineDirection(line, board):
    if (line % (2 * board + 1) <= board):
        return 'horizontal'  # pozioma linia
    else:
        return 'vertical'  # pionowa linia


print(lineDirection(5, 2))

# class Game():

#     def __init__(self, board):
#         # Code here

#     def play(self, lines):
#         # Code here


# print("Example tests")

# original = [1, 3, 4]
# result = [1, 3, 4, 6]
# game = Game(2)
# print("Should return: '"+str(result)+"'")
# print(game.play(original), result)

# original = [7, 9, 12]
# result = [7, 9, 10, 12]
# game = Game(2)
# print("Should return: '"+str(result)+"'")
# print(game.play(original), result)

# original = [1, 2, 3, 4, 5, 8, 10, 11, 12]
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# game = Game(2)
# print("Should return: '"+str(result)+"'")
# print(game.play(original), result)

# original = []
# result = []
# game = Game(2)
# print("Should return: '"+str(result)+"'")
# print(game.play(original), result)
