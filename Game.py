import numpy as np
from Puzzles import *
import itertools
"""
Game logic

"""
original = []
game_board = []
backup = []
np.random.seed(42)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def game_generator(level) :
    global game_board, original
    original = next(itertools.islice((z for z in problemSet), level, None))
    game_board = np.copy(original)

    return original


def generate_empty_game():
    global game_board
    game_board = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(0)
        game_board.append(row)
    return game_board


def solve():
    global game_board
    shuffled = np.copy(numbers)

    for i in range(9):
        for j in range(9):
            if game_board[i][j] == 0:
                for val in shuffled:
                    if is_valid(i, j, val):
                        game_board[i][j] = val
                        if solve():
                            return True
                        else:
                            game_board[i][j] = 0
                return False
    return True


def in_row(row, col, val):
    global game_board
    line = game_board[row]
    for i in range(len(line)):
        if i == col:
            continue
        elif line[i] == val:
            return True

    return False


def in_col(row, col, val):
    global game_board

    for i in range(9):
        if i == row:
            continue
        elif game_board[i][col] == val:
            return True

    return False


def in_box(row, col, val):
    global game_board
    row_offset = (row // 3) * 3
    col_offset = (col // 3) * 3

    x = set()

    for i in range(3):
        for j in range(3):
            if i + row_offset == row and j + col_offset == col:
                continue
            else:
                if val in x:
                    return True
                x.add(game_board[row_offset + i][col_offset + j])

    return False


def set_val(row, col, val):
    global game_board
    game_board[row][col] = val
    return


def is_valid(row, col, val):
    print(game_board)
    return not in_box(row, col, val) and not in_col(row, col, val) and not in_row(row, col, val)


def get_game(number):
    global original, game_board
    original = problemSet[number]
    game_board = np.copy(game_board)

    return original


def set_board(board):
    global game_board
    game_board = board
    return


def print_board(board=game_board):
    for i in range(9):
        print(board[i])


def return_solved():
    global game_board
    game_board = np.copy(original)
    solve()
    return game_board
