#!/usr/bin/python3

"""
function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    load_from_json_file
    function that creates an Object to a text file from a JSON file
    Parameters: filename
    Returns: json object
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
