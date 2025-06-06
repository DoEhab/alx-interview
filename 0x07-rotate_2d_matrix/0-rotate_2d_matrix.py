#!/usr/bin/python3
"""
rotate a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotate a 2d matrix in place
    :param matrix: the matrix to be rotated
    :return: None
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
