#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        count = len(x)
        for i in range(count):
            length = count - 1
            if i < (length):
                print("{:d} ".format(x[i]), end="")
            else:
                print("{:d}".format(x[i]))
