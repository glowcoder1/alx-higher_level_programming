#!/usr/bin/python3

def max_integer(my_list=[]):
    count = len(my_list)
    if count > 0:
        return sorted(my_list)[count - 1]
    return None
