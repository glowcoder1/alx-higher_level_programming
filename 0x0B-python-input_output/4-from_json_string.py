#!/usr/bin/python3

"""
from_json_string
"""


import json


def from_json_string(my_obj):
    """
    from_json_string
    function that returns the JSON representation of an object (string)
    Parameters: my_obj
    Returns: JSON
    """
    return json.load(my_obj)
