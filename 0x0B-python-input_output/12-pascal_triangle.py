#!/usr/bin/python3

"""
Paschal's triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the
    Pascal’s triangle of n
    """

    res = []
    if n <= 0:
        return res
    res.append([1])
    if n == 1:
        return res
    for i in range(1, n):
        prev = res[i - 1]
        curr = [1]
        prevlen = len(prev)
        for j in range(0, prevlen - 1):
            val = prev[j]
            if (prev[j + 1]):
                val += prev[j + 1]
            curr.append(val)
        curr.append(1)
        res.append(curr)
    return res
