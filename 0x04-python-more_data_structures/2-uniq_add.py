#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = list(set(my_list))
    res = 0
    for n in uniq:
        res += n
    return res
