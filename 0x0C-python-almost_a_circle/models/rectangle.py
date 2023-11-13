#!/usr/bin/python3

"""
Module for Rectangle class which
inherits the Base class
"""

from models.base import Base


class Rectangele(Base):
    """
    Rectangle class that inherits from Base
    Args:
    width
    height
    x
    y
    id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
