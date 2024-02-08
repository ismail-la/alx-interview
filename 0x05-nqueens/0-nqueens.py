#!/usr/bin/python3
"""N Queens problem Solution module"""

import sys


def Get_solutions(ro, col):
    resolution = [[]]
    for queen in range(ro):
        resolution = queen_position(queen, col, resolution)
    return resolution


def queen_position(queen, col, prev_resolution):
    safe_place = []
    for array in prev_resolution:
        for i in range(col):
            if is_queen_placement_safe(queen, i, array):
                safe_place.append(array + [i])
    return safe_place


def is_queen_placement_safe(q, i, array):
    """checks if placing a queen.
    -q:  is likely the column index we're trying to check for safety.
    -i: is the row index we're considering placing the queen in.
    -array: represents the current arrangement of queens on the board.
    """
    if i in array:
        return (False)
    else:
        return all(abs(array[column] - i) != q - column
                   for column in range(q))


def init():
    """ initialization of the program
    The function checks if the number of command-line arguments provided
    is exactly 2. If not, it prints a usage message and exits the program
    with an error code of 1.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        N = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (N)


def Nqueens():

    N = init()
    solutions = Get_solutions(N, N)
    for array in solutions:
        clean = []
        for q, i in enumerate(array):
            clean.append([q, i])
        print(clean)


if __name__ == '__main__':
    Nqueens()
