#!/usr/bin/python3
"""
module that creates  aSquare class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    Private attributes: size
    Inherits BaseGeometry.
    """

    def __init__(self, size):
        """Initializes class attributes

        Parameters:
        width: width of the rectangle
        heigth: height of the rectangle
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

     def __str__(self):
        """Return: formatted string."""

        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Computes a square's area.
        Overwrites the area mtd  inherited from Rectangle.
        """

        return self.__size * self.__size
