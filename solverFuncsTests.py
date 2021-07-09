# Project 3 - Calcudoku Solver
#
# Author: Abbey Towse
# Section: CPE 101-11
# Date: 4/24/2021

import unittest
from solverFuncs import *


class TestCases(unittest.TestCase):
    def test_check_row_valid_0(self):
        puzzle = [[0] * 5] * 5
        self.assertEqual(check_rows_valid(puzzle), True)

    def test_check_columns_valid_0(self):
        puzzle = [[0] * 5] * 5
        self.assertEqual(check_columns_valid(puzzle), True)

    def test_check_cages_valid_0(self):
        puzzle = [[0] * 5] * 5
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_cages_valid(puzzle, cages), True)

    def test_check_valid_0(self):
        puzzle = [[0] * 5] * 5
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_valid(puzzle, cages), True)

    def test_check_row_valid_1(self):
        puzzle = [[1] * 5] * 5
        self.assertEqual(check_rows_valid(puzzle), False)

    def test_check_columns_valid_1(self):
        puzzle = [[1] * 5] * 5
        self.assertEqual(check_columns_valid(puzzle), False)

    def test_check_cages_valid_1(self):
        puzzle = [[1] * 5] * 5
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_cages_valid(puzzle, cages), False)

    def test_check_valid_1(self):
        puzzle = [[1] * 5] * 5
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_valid(puzzle, cages), False)

    def test_check_rows_valid_2(self):
        puzzle = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3],
                  [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
        self.assertEqual(check_rows_valid(puzzle), False)

    def test_check_columns_valid_2(self):
        puzzle = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3],
                  [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
        self.assertEqual(check_columns_valid(puzzle), True)

    def test_check_cages_2(self):
        puzzle = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3],
                  [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_cages_valid(puzzle, cages), False)

    def test_check_valid_2(self):
        puzzle = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3],
                  [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_valid(puzzle, cages), False)

    def test_check_rows_valid_3(self):
        puzzle = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                  [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        self.assertEqual(check_rows_valid(puzzle), True)

    def test_check_columns_valid_3(self):
        puzzle = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                  [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        self.assertEqual(check_columns_valid(puzzle), False)

    def test_check_cages_3(self):
        puzzle = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                  [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_cages_valid(puzzle, cages), False)

    def test_check_valid_3(self):
        puzzle = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
                  [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_valid(puzzle, cages), False)

    def test_check_cages_valid_4(self):
        puzzle = [[5, 3, 2, 1, 4], [5, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_cages_valid(puzzle, cages), False)

    def test_check_cages_valid_5(self):
        puzzle = [[4, 3, 2, 1, 5], [5, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_cages_valid(puzzle, cages), False)

    def test_check_cages_valid_6(self):
        puzzle = [[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 5, 5, 3],
                  [1, 2, 4, 3, 5], [4, 5, 0, 0, 0]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_cages_valid(puzzle, cages), False)

    def test_check_valid_7(self):
        puzzle = [[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 1, 5, 3],
                  [1, 2, 4, 3, 5], [4, 3, 5, 2, 1]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_valid(puzzle, cages), True)

    def test_check_valid_8(self):
        puzzle = [[3, 5, 2, 1, 4], [5, 1, 3, 4, 2], [2, 4, 5, 5, 3],
                  [1, 2, 4, 3, 5], [4, 5, 0, 0, 0]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_valid(puzzle, cages), False)

    def test_check_valid_9(self):
        puzzle = [[1, 2, 3, 4, 5], [5, 5, 3, 2, 1], [3, 2, 1, 4, 5],
                  [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_valid(puzzle, cages), False)

    def test_check_valid_10(self):
        puzzle = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cages = [[9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]
        self.assertEqual(check_valid(puzzle, cages), True)

    def test_check_valid_11(self):
        puzzle = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
        cages = [[6, 3, 0, 5, 10], [18, 5, 1, 2, 3, 7, 8], [5, 1, 4],
                 [17, 4, 6, 11, 12, 16], [4, 3, 9, 13, 14], [10, 3, 15, 20, 21],
                 [15, 6, 17, 18, 19, 22, 23, 24]]
        self.assertEqual(check_valid(puzzle, cages), True)

    def test_check_valid_12(self):
        puzzle = [[4, 1, 5, 2, 3], [1, 2, 4, 3, 5], [5, 4, 3, 1, 2],
                  [2, 3, 1, 5, 4], [3, 5, 2, 4, 1]]
        cages = [[7, 3, 0, 1, 6], [18, 5, 2, 3, 4, 8, 9], [23, 7, 5, 10, 11, 15, 16, 20, 21],
                 [15, 6, 7, 12, 17, 22, 23, 24], [12, 4, 13, 14, 18, 19]]
        self.assertEqual(check_valid(puzzle, cages), True)

    def test_check_valid_13(self):
        puzzle = [[4, 1, 5, 2, 3], [1, 2, 4, 3, 5], [5, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cages = [[7, 3, 0, 1, 6], [18, 5, 2, 3, 4, 8, 9], [23, 7, 5, 10, 11, 15, 16, 20, 21],
                 [15, 6, 7, 12, 17, 22, 23, 24], [12, 4, 13, 14, 18, 19]]
        self.assertEqual(check_valid(puzzle, cages), False)

    def test_check_row_valid_14(self):
        puzzle = [[4, 1, 5, 2, 3], [1, 2, 4, 3, 5], [5, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(check_rows_valid(puzzle), True)

    def test_check_columns_valid_15(self):
        puzzle = [[4, 1, 5, 2, 3], [1, 2, 4, 3, 5], [5, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(check_columns_valid(puzzle), False)

    def test_check_cages_valid_16(self):
        puzzle = [[4, 1, 5, 2, 3], [1, 2, 4, 3, 5], [5, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        cages = [[7, 3, 0, 1, 6], [18, 5, 2, 3, 4, 8, 9], [23, 7, 5, 10, 11, 15, 16, 20, 21],
                 [15, 6, 7, 12, 17, 22, 23, 24], [12, 4, 13, 14, 18, 19]]
        self.assertEqual(check_cages_valid(puzzle, cages), True)


if __name__ == '__main__':
    unittest.main()
