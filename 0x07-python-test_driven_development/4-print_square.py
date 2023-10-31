#!/usr/bin/python3

"""
Print square module
"""


def print_square(size):
    """
    prints a square with the character #
    Return: None
    """

    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
