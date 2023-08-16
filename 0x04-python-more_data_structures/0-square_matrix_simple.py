#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for row in matrix:
        res.append(list(n ** 2 for n in row))
    return res
