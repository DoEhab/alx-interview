#!/usr/bin/python3
"""
island_perimeter
"""


def island_perimeter(grid):
    """
    method to calculate the perimeter
    :param grid: 0-1 matrix
    :return: perimeter
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if j + 1 < cols and grid[i][j + 1] == 1:
                    perimeter -= 2
                if i + 1 < rows and grid[i + 1][j] == 1:
                    perimeter -= 2

    return perimeter
