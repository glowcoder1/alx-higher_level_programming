#!/usr/bin/python3


"""
Text indentation module
This module provides the function text_indentation
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Return None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip = False
    for char in text:
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
            skip = True
        elif skip:
            skip = False
            if char == " ":
                continue
            print(char, end="")
        else:
            print(char, end="")
