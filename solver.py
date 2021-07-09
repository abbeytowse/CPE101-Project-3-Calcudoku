# Project 3 - Calcudoku Solver
#
# Author: Abbey Towse
# Section: CPE 101-11
# Date: 4/24/2021

from solverFuncs import *


def main():
    # set 5 x 5 puzzle
    puzzle = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]

    # create cages from user input
    cages = get_cages()

    # set location to puzzle[0][0]
    location = 0

    # create counters
    count_checks = 0
    count_backtracks = 0

    # create loop based on location in puzzle
    while 0 <= location < len(puzzle) ** 2:
        # 0 will always be the lowest location in the puzzle
        # max location in puzzle is length of puzzle squared minus one

        # given a square puzzle length of puzzle will be the denominator
        row = location // len(puzzle)
        # number of times denominator goes into numerator gives
        # 1st dimension's index
        col = location % len(puzzle)
        # remainder gives 2nd dimension's index

        puzzle[row][col] += 1    # increase index's value by 1
        count_checks += 1

        # check new index value is valid
        if puzzle[row][col] > len(puzzle):
            # ensure index value is not greater than length of puzzle

            puzzle[row][col] = 0    # reset value at index to 0
            location -= 1    # move backwards
            count_backtracks += 1

        else:

            if check_valid(puzzle, cages):
                # check validity of rows, columns, and cages

                location += 1    # move forward

    # print output
    print("\n--Solution--\n")

    for i in range(len(puzzle)):
        # print puzzle as a matrix rather than a list of lists

        print(*puzzle[i], sep='  ')
        # code from kite.com

    print("\nchecks: ", count_checks, end='')
    # prints checks & backtracks on same line
    print(" backtracks: ", count_backtracks)


# run main
main()
