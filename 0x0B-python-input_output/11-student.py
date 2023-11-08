#!/usr/bin/python3

"""
module for student class with  with filter
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

    def to_json(self, attrs=None):
        """ returns the filtered dictionary rep of the instance"""

        if (type(attrs) == list):
            if all(type(elem) == str for elem in attrs):
                return {attr: getattr(self, attr) for attr in attrs
                        if hasattr(self, attr)}

        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """

        for key, val in json.items():
            setattr(self, key, val)
