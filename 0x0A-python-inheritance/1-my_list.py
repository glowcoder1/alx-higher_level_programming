#!/usr/bin/python3

"""
print sorted
"""

class MyList(list):
    """MyList class"""
    def print_sorted(self):
    """
    prints sorted list
    Paramters: self
    Returns: none
    """
    temp = self.copy()
    temp.sort()
    print(temp)
