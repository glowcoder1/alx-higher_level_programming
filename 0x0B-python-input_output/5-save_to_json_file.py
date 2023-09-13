#!/usr/bin/python3

"""
function that writes a string to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file
    function that writes an Object to a text file, using a JSON representation
    Parameters: my_obj, filename
    Returns: none
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
