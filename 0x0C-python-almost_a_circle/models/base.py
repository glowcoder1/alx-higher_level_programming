#!/usr/bin/python3

"""
Base class module
"""


class Base:
    """
    base class for managig id attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON str rep of a list of dicts.

        Accepts:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Accepts:
            list_objs (list): A list of inherited Base instances.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dict_list = [d.to_dictionary() for d in list_objs]
                jsonfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):

        """returns the list of the JSON string representation json_string

        Accepts:
            json_string:  A JSON str rep of a list of dicts.
        Returns:
            Empty file if json_string is None or empty.
            Else, the list represented by json_string.
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """Returns an instance from a dictionary of attrs.
        Accepts:
            **dict: Key/value pairs of attr to initialize.
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_cls = cls(1, 1)
            else:
                new_cls = cls(1)
            new_cls.update(**dictionary)
            return new_cls

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes from a JSON string file

        Reads from `<cls.__name__>.json`.

        Returns:
            an empty list if file doesn't exist.
            else, a list of instantiated classes.
        """

        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as jsonfile:
                dict_list = Base.from_json_string(jsonfile.read())
                return [cls.create(**item) for item in dict_list]
        except IOError:
            return []
