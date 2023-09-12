#!/usr/bin/python3

"""
function that appends a string to a text file
"""


def append_write(filename="", text=""):
    """
    append_write
    function that append a string to a text file
    Parameters: filename, text
    Returns: no of chars added
    """

    with open(filename, "a") as f:
        charsWritten = f.write(text)
        return charsWritten
