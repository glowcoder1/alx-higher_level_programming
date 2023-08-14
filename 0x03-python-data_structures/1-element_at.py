#!/usr/bin/python3

def element_at(my_list, idx):
    count = len(my_list)
    if idx < 0 or count == 0 or idx > (count - 1):
        return None
    return my_list[idx]
