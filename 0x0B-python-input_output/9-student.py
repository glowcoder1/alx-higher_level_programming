#!/usr/bin/python3

"""
module for student class
"""


class Student:
    """
    student class
    attributes: first_name, last_name, age
    methods: to_json
    """

    def __init__(self, first_name, last_name, age):
        """
        creates student instance
        Args: first_name, last_name, age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns the dictionary rep of the instance"""

        return self.__dict__
