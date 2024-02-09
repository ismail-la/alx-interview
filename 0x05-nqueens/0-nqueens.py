#!/usr/bin/python3
"""
    Description: The N queens puzzle is the challenge of placing N non-attacking 
                 queens on an NxN chessboard. Write a program tha solve the N
                 queens problem.

    Usage: nqueen4s N:
            If the user called the program with the wrong number of arguments,
            print usage: nqueens N, followed by a new line, and exist with the
            status 1
    Where N must be an integer greater or equal to 4:
            If N is not an integer, print N must be a number, followed by a new
            line, and exist with the status 1
            If N is smaller than 4, print N must be at least 4, followed by new 
            line, and exit with the status 1
    The programe should print every possible solution to the problem:
            One solution per line
            Format: see example
            you don't have to print the solution in a specific order
    You are only allowed to import the sys module 
"""

import sys

def print_board(board):
    """ print_board 
    Args:
        board - list of list with length sys.argv[1]
    """
    new_list = []
    for i, row in enumerate(board):
        value = []
        for j, col in enumerate(row):
            if col == 1:
                value.append(i)
                value.append(j)
        new_list.append(value)

    print(new_list)


def isSafe(board, row, col, number):
    """ isSafe
    Args:
        board - list of list with length sys.argv[1]
        row - row to check if is safe doing a movement in this position
        col - col to check if is safe doing a movement in this position
        number: size of the board
    return: True or False
    """

    #check this row in the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
            
    #check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    for i, j in zip(range(row, number, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    return True

def solveNQUtil(board, col, number):
    """ Auxiliar method to find the posibilities of answer
    Args:
        board - board to resolve
        col - number of col
        number - size of the board
    returns:
        All the posibilities to solve the problem
    """

    if (col == number):
        print_board(board)
        return True
    res = False
    for i in range(number):

        if (isSafe(board, i, col, number)):
            #place this queen in board[1][col]
            board[i][col] = 1

            #make result true if any placement is possible
            res = solveNQUtil(board, col + 1, number) or res

            board[i][col] = 0 #backtrack

    return res

def solve(number):
    """ Find all the posibilities if exists 
    Args:
        number - size of the board
    """
    board = [[0 for i in range(number)]for i in range(number)]

    if not solveNQUtil(board, 0, number):
        return False
    
    return True

def validate(args):
    """ Validate the input data to verify if the size to
        answer is possible
    Args:
        args - sys.argv
    """
    if (len(args) == 2):
        #validate data
        try:
            number = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    """ Main method ro execute the application
    """

    number = validate(sys.argv)
    solve(number)
