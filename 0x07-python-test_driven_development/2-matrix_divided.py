#!/usr/bin/python3

"""
2-matrix_divided module
This module provides the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    matrix_divided divides all elements of a matrix.
    Returns a new matrix
    """
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix):
        new_matrix = []
        for row in matrix:
            rowLen = len(row)
            if rowLen != len(matrix[0]):
                raise TypeError(
                    "Each row of the matrix must have the same size")
            if rowLen:
                new_row = []
                for value in row:
                    if (isinstance(value, int) or isinstance(value, float)):
                        new_row.append(round(value/div, 2))
                    else:
                        raise TypeError("matrix must be a matrix (list of "
                                        "lists) of integers/floats")
                new_matrix.append(new_row)
            else:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
        return new_matrix
    else:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
