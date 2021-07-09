# Project 3 - Calcudoku Solver
#
# Author: Abbey Towse
# Section: CPE 101-11
# Date: 4/24/2021


def get_cages():

    """
    Input type: string
    Output type: list
    Function: gets user input to create list of cages
    """

    # prompt user for number of cages and store
    num_cages = input("Number of cages: ")
    num_cages = int(num_cages)    # convert input from str to int

    # create empty list to store user cage input within
    cages = []

    # create loop based on user input for num_cages
    for i in range(num_cages):

        num_cages = i

        # prompt user for cage
        cage = input("Cage number " + str(num_cages) + ": ").split()
        cage = list(map(int, cage))
        # code to convert list from str to int from GeeksForGeeks
        cages.append(cage)    # adds user input to cages list

    return cages    # returns list with all cages within it


def check_rows_valid(puzzle):

    """
    Input type: list
    Output type: boolean
    Function: checks a given list for repeat values,
    if repeats present returns false
    """

    # given puzzle is square, creates a loop based on puzzle length
    for row in range(len(puzzle)):

        # pull out each list within the list individually
        list_a = puzzle[row]

        # creates loop to check each index in list_a
        for index in range(len(list_a)):

            # checks if any value occurs more than once, excluding 0
            if list_a.count(index + 1) <= 1:

                pass    # continue checking if no repeats

            else:

                return False    # return False if repeats

    return True    # returns True if no list contains repeats


def check_columns_valid(puzzle):

    """
    Input type: list
    Output type: boolean
    Function: checks if the same index of different lists have the
    same value, if they do returns false
    """

    # given puzzle is square, creates a loop based on puzzle length
    for col in range(len(puzzle)):

        # create empty list to store the same index of different lists
        # for comparison
        element_list = []

        # set the max index value for lists within the list
        row = len(puzzle) - 1

        # create loop ensuring first dimension index is positive
        while row >= 0:

            element_list.insert(0, puzzle[row][col])
            # adds value at index to comparison list
            row -= 1    # move to another list

        # creates loop to check each index in element_list
        for index in range(len(element_list)):

            # checks if any value occurs more than once, excluding 0
            if element_list.count(index + 1) <= 1:

                pass    # continue checking if no repeats

            else:

                return False    # return False if repeats

    return True    # returns True if no list contains repeats


def check_cages_valid(puzzle, cages):

    """
    Input type: lists
    Output type: boolean
    Function: checks if specified indexes sum to the expected value
    """

    for index in range(len(cages)):

        # determine what the finished cage should sum to
        expected_sum = cages[index][0]
        actual_sum = 0    # record actual cage sum

        # get length of cage within cages
        length_of_cage = len(cages[index])
        # determine how many indexes in the cage contain location info
        iterations = length_of_cage - 2

        # create empty list to store indexes with location info
        location_info = []

        # will track index within location info list
        element = 0

        # create loop based on how many indexes contain location info
        for j in range(iterations):

            # grab location information for each index by skipping first
            # two values within the index
            location = cages[index][j + 2]

            # given a square puzzle length of puzzle will be the denominator
            row = location // len(puzzle)
            # number of times denominator goes into numerator gives
            # 1st dimension's index
            col = location % len(puzzle)
            # remainder gives 2nd dimension's index

            # adds value at location to location info list
            location_info.append(puzzle[row][col])

        # create loop that stops summing at end of location info list
        while element < len(location_info):

            # adds value at index to actual cage total
            actual_sum += location_info[element]
            element += 1    # moves to next index in the list
            # while loop logic from GeeksForGeeks

        # checks if cage sum is what it should be & if cage is incomplete
        if actual_sum == expected_sum or actual_sum == 0:

            pass
            # continue checking if actual total equals expected
            # or if cage has no value yet

        elif actual_sum > expected_sum:
            # checks if actual total exceeds expected total

            return False    # return false if actual total exceeds expected

        elif location_info.count(0) >= 1:
            # checks if cage is incomplete

            pass    # continue checking if cage incomplete

        elif actual_sum < expected_sum:
            # checks if completed cage sum is less than expected

            return False
            # returns false is completed cage sum is less than expected

    return True    # returns True is all cages are valid


def check_valid(puzzle, cages):

    """
    Input type: lists
    Output type: boolean
    Function: given puzzle and cages checks if all conditions are met
    """

    # checks for repeat and that specified indexes sum as expected
    if check_rows_valid(puzzle) and check_columns_valid(puzzle) and \
            check_cages_valid(puzzle, cages):

        return True    # returns true if no repeats and expected sums

    else:

        return False   # returns false if repeats or unexpected sums
