#!/usr/bin/python3

"""
Module for Rectangle class which
inherits the Base class
"""

from models.base import Base


class Rectangle(Base):
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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of the Rectangle Instance"""

        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """

        rect = ""
        if self.__width == 0 or self.__height == 0:
            print(rect)
            return
        rect += "\n" * self.y
        for i in range(self.__height):
            rect += " " * self.x
            rect += "#" * self.__width
            if i != self.__height - 1:
                rect += "\n"
        print(rect)

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:.

        *args: attribute to be updated.
        - 1st argument reps id attribute
        - 2nd argument reps width attribute
        - 3rd argument rep height attribute
        - 4th argument reps x attribute
        - 5th argument reps y attribute

        **kwargs: key/val of attributes to update
        """

        args_len = len(args)
        if args and args_len != 0:
            for i in range(args_len):
                arg = args[i]
                if i == 0:
                    self.__init__(self.width, self.height, self.x, self.y,
                                  arg)
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.__init__(self.width, self.height, self.x, self.y,
                                  v)
                elif k in ["width", "height", "x", "y"]:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary rep of Rectangle Instance."""

        return {
            "height": self.height,
            "width": self.width,
            "x": self.x,
            "y": self.y,
            "id": self.id,
        }
