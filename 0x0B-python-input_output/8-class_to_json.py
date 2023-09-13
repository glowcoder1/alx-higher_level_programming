#!/usr/bin/python3

"""
My class to json  module
"""


def class_to_json(obj):
    """
    class_to_json
    returns the dictionary description with simple data structure
    Parametrs: obj
    Returns: the dictionary description
    """
    return obj.__dict__
