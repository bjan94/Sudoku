from random import seed, shuffle, random
import numpy as np
from Puzzles import *
"""
Game logic

"""
game_board = []
np.random.seed(42)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


game_generator = (x for x in problemSet)


def generate_empty_game():
    global game_board
    game_board = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(0)
        game_board.append(row)
    return game_board


def generate_game():
    return game_board


def fill_box(row_offset, col_offset):
    global game_board
    start_row = row_offset * 3
    start_col = col_offset * 3
    shuffled = np.copy(numbers)
    np.random.shuffle(shuffled)

    for i in range(3):
        for j in range(3):
            for val in shuffled:
                if is_valid(start_row + i, start_col + j, val):
                    game_board[start_row + i][start_col + j] = val


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


def in_row(row, val):
    global game_board
    line = game_board[row]

    return val in line


def in_col(col, val):
    global game_board

    for i in range(9):
        if game_board[i][col] == val:
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


def is_valid(row, col, val):
    return not in_box(row, col, val) and not in_col(col, val) and not in_row(row, val)


def get_game(number):
    global game_board
    game_board = problemSet[number]
    return game_board


def set_board(board):
    global game_board
    game_board = board
    return


def print_board(board=game_board):
    for i in range(9):
        print(board[i])
