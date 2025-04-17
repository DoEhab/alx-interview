#!/usr/bin/python3
"""
0-pascal triangle
"""


def pascal_triangle(n):
    """
    pascal function
    :param n: the triangle size
    :return: list of list containing all rows of triangle
    """
    if n <= 0:
        return []
    pascal_list = [[1]]
    for i in range(1, n):
        current_list = pascal_list[i - 1]
        temp_list = [1]
        for j in range(1, i):
            temp_list.append(current_list[j - 1] + current_list[j])
        temp_list.append(1)
        pascal_list.append(temp_list)

    return pascal_list







