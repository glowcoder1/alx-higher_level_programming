#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = {}
    if a_dictionary:
        new_dict = {key: value for (key, value) in a_dictionary.items()}
    new_dict[key] = value
    return new_dict
