#!/usr/bin/python3
"""
module that creates a BaseGeometry class.
"""


class BaseGeometry:
    """ BaseGeometry
    methods: area, interger_validator
    """

    def area(self):
        """Raises an Exception
        'area() is not implemented'.
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates that value is integer."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
