#!/usr/bin/python3

"""
function that appends a string to a text file
"""


def append_file(filename="", text=""):
    """
    append_file
    function that append a string to a text file
    Parameters: filename, text
    Returns: no of chars added
    """

    with open(filename, "a") as f:
        charsWritten = f.write(text)
        return charsWritten
