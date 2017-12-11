import unittest

from Game import *


class SudokuTest(unittest.TestCase):
    sample_board = [[2, 9, 6, 3, 1, 8, 5, 7, 4],
                  [5, 8, 4, 9, 7, 2, 6, 1, 3],
                  [7, 1, 3, 6, 4, 5, 2, 8, 9],
                  [6, 2, 5, 8, 9, 7, 3, 4, 1],
                  [9, 3, 1, 4, 2, 6, 8, 5, 7],
                  [4, 7, 8, 5, 3, 1, 9, 2, 6],
                  [1, 6, 7, 2, 5, 3, 4, 9, 8],
                  [8, 5, 9, 7, 6, 4, 1, 3, 2],
                  [3, 4, 2, 1, 8, 9, 7, 6, 5]]

    def testInBox(self):
        # self.assertTrue(in_box(2, 2, 6, self.sample_board))
        # self.assertFalse(in_box(4, 5, 6, self.sample_board))
        pass

    def test_generate(self):
        generated_board = generate_game()
        print_board(generated_board)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
