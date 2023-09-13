#!/usr/bin/python3
"""
module that creates a Rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    Private attributes: width, height
    Inherits BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes class attributes

        Parameters:
        width: width of the rectangle
        heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

     def __str__(self):
        """Return: formatted string."""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Computes rectangle's area.
        Overwrites the area mtd  inherited from BaseGeometry.
        """

        return self.__width * self.__height
