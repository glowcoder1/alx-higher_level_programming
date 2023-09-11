#!/usr/bin/python3

"""
provides inherits_from func
"""

def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Parameters: obj, a_class
    Returns: true or false

    """
    if isinstance(a_class, type(obj)):
        return True
    return False
