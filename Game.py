from random import seed, shuffle, random
import numpy as np
"""
Game logic

"""
game_board = []
np.random.seed(42)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
    global game_board
    game_board = generate_empty_game()
    shuffled = np.copy(numbers)
    np.random.shuffle(shuffled)

    # Top Left box is just shuffled array
    for i in range(3):
        for j in range(3):
            game_board[i][j] = shuffled[i + j]

    # Fill the rest of the grid
    for i in range(3):
        for j in range(3):
            if i == 0 and j == 0:
                continue
            else:
                fill_box(i, j)

    return game_board


def fill_box(row_offset, col_offset):
    global game_board
    start_row = row_offset * 3
    start_col = col_offset * 3
    shuffled = np.copy(numbers)
    np.random.shuffle(shuffled)

    for i in range(3):
        for j in range(3):
            while game_board[start_row + i][start_col + j] == 0:
                for val in shuffled:
                    if (
                        not in_row(start_row + i, val)
                        and not in_col(start_col + j, val)
                        and not in_box(start_row + i, start_col + j, val)
                    ):
                        game_board[start_row + i][start_col + j] = val



def solve(game_state):
    pass


def in_row(row, val):
    global game_board
    x = set()
    for i in range(9):
        if row == i:
            continue
        elif val in x:
            return True
        x.add(game_board[row][i])

    return False


def in_col(col, val):
    global game_board
    x = set()
    for i in range(9):
        if col == i:
            continue
        elif val in x:
            return True
        x.add(game_board[i][col])

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


def print_board(board=game_board):
    for i in range(9):
        print(board[i])
