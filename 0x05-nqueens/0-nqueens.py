import sys

def is_not_under_attack(queens_pos, row, col):
    for queen_row, queen_col in queens_pos:
        if queen_row == row or queen_col == col or queen_row + queen_col == row + col or queen_row - queen_col == row - col:
            return False
    return True

def solve_nqueens(n, row, queens_pos, solutions):
    if row == n:
        solutions.append(queens_pos[:])  # Found a valid solution
        return
    for col in range(n):
        if is_not_under_attack(queens_pos, row, col):
            queens_pos.append((row, col))
            solve_nqueens(n, row + 1, queens_pos, solutions)
            queens_pos.pop()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(N, 0, [], solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

