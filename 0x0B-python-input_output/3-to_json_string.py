#!/usr/bin/python3
import json

"""
to_json_string
"""


def to_json_string(my_obj):
    """
    to_json_string
    function that returns the JSON representation of an object (string)
    Parameters: my_obj
    Returns: JSON
    """
    return json.dumps(my_obj)
