#!/usr/bin/python3

"""
Module provides is kind func
"""


def is_kind_of_class(obj, a_class):
    """
    checks  if the object is an instance of, or if the object is an instance of
    a class that inherited from the specified class
    """
    if isinstance(obj, a_class) or issubclass(a_class, type(obj)):
        return True
    return False
