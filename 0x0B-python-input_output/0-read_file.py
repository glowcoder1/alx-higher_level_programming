#!/usr/bin/python3

"""
module for read_file
"""


def read_file(filename=""):
    with open(filename) as f:
        print(f.read())
