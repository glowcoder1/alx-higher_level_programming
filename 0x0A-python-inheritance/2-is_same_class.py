#!/usr/bin/python3

"""
This module provides is_same_class func
"""


def is_same_class(obj, a_class):
    """
    returns true or false if obj belongs to same class
    Parameters: obj, a_class
    Returns: True or false
    """
    if type(obj) is a_class:
        return True
    return False
