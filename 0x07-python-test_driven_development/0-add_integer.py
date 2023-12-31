#!/usr/bin/python3

"""
add_integer module
This module provides the add integer funtion
"""


def add_integer(a, b=98):
    """
    add_integer adds 2 integers
    Returns the sum of added integer
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
