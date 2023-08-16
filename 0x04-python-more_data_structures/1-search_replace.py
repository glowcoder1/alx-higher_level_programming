#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = []
    for val in my_list:
        if val == search:
            val = replace
        res.append(val)
    return res
