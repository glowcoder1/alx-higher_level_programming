#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len (tuple_b)
    a = 0
    b = 0
    c = 0
    d = 0
    if len_a == 2:
        a, b = tuple_a
    elif len_a > 2:
        a = tuple_a[0]
        b = tuple_a[1]
    elif len_a == 1:
        a = tuple_a[0]
    if len_b == 2:
        c, d = tuple_b
    elif len_b > 2:
        c = tuple_b[0]
        d = tuple_b[1]
    elif len_b == 1:
        c = tuple_b[0]
    return (a + c, b + d)
