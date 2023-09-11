#!/usr/bin/python3

"""
This modue provides the look up func

Functions:
lookup

"""


def lookup(obj):
    """
    lookup takes a class and returns list of attr and mtds
    Parameter:
    obj
    Returns:
    list of attr and mtds
    """
    return(dir(obj))
