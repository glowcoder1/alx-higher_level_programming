#!/usr/bin/python3

"""
to_json_string
"""


import json


def to_json_string(my_obj):
    """
    to_json_string
    function that returns the JSON representation of an object (string)
    Parameters: my_obj
    Returns: JSON
    """
    return json.dumps(my_obj)
