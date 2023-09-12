#!/usr/bin/python3

"""
function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    write_file
    function that writes a string to a text file
    Parameters: filename, text
    Returns: no of chars written
    """

    with open(filename, "w") as f:
        charsWritten = f.write(text)
        return charsWritten
