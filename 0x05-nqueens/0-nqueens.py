#!/usr/bin/python3
"""N Queens problem Solution module"""

import sys


def get_solutions(ro, col):
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
    if i in array:
        return False
    else:
        return all(abs(array[column] - i) != q - column
                   for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N


def Nqueens():
    N = init()
    solutions = get_solutions(N, N)
    for array in solutions:
        clean = []
        for q, i in enumerate(array):
            clean.append([q, i])
        print(clean)


if __name__ == '__main__':
    Nqueens()
