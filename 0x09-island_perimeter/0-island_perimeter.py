#!/usr/bin/python3
""" Island Perimeter problem """


def island_perimeter(grid):
    """Calculates the Perimeter of an island"""
    perimeter = 0
    for i in range(len(grid)):
        for cell_index in range(len(grid[0])):
            current_cell = grid[i][cell_index]
            if not current_cell:
                continue
            upper_cell = None if not i else \
                grid[i - 1][cell_index]
            left_cell = None if not cell_index else \
                grid[i][cell_index - 1]
            cell_perimeter = 4
            if upper_cell:
                cell_perimeter = cell_perimeter - 2
            if left_cell:
                cell_perimeter = cell_perimeter - 2
            perimeter = perimeter + cell_perimeter
    return perimeter
