#!/usr/bin/python3

"""
module for read_file
"""


def read_file(filename=""):
    """
    read_file
    Parameters: filename
    Returns: None, prints to stdout
    """
    with open(filename) as f:
        print(f.read(), end="")
