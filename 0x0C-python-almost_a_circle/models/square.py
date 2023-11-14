#!/usr/bin/python3

"""square class module."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square class."""

    def __init__(self, size, x=0, y=0, id=None):

        """Initialize a new instance of Square class.
        size (int): The size of the Square.
        x (int): The x coord of the Square.
        y (int): The y coord of the Square.
        id (int): The id of the new Square instance.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the Square Instance."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square.

         *args: attribute to be updated.
         - 1st argument reps id attribute
         - 2nd argument reps size attribute
         - 3rd argument reps x attribute
         - 4th argument reps y attribute
         **kwargs: key/val of attributes to update

         """

        args_len = len(args)
        if args and args_len != 0:
            for i in range(args_len):
                arg = args[i]
                if i == 0:
                    self.__init__(self.width, self.height, self.x,
                                  self.y, arg)
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.__init__(self.width, self.height, self.x, self.y
                                  v)
                elif k in ["x", "y", "size"]:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary rep of Square Instance."""

        return {
            "size": self.width,
            "x": self.x,
            "y": self.y,
            "id": self.id,
        }

    def __str__(self):
        """Returns the print() and str() rep of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
