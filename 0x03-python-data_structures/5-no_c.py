#!/usr/bin/python3

def no_c(my_string):
    new_s = ""
    for val in my_string:
        if val != "c" and val != "C":
            new_s = new_s + val
    return new_s
