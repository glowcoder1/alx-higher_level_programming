#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    count = len(my_list)
    new_l = []
    for val in my_list:
        new_l.append(val)
    if idx < 0 or count == 0 or idx > (count - 1):
        return new_l
    new_l[idx] = element
    return new_l
