#!/usr/bin/python3
"""module: models"""


class Base:
    """class: Base"""

    __nb_objects = 0
    """The number of instances extending this"""

    def val_int(self, name, val, mess):
        """Validate an int and throw an error if something's wrong"""
        pass

    def __init__(self, id=None):
        """Init"""
        pass

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of cls with attributes already set"""
        pass

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a json string representation of a list of dictionaries"""
        pass

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries represented by a json string"""
        pass

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of objs to file in json form"""
        pass

    @classmethod
    def load_from_file(cls):
        """Load list of objs from file in json form"""
        pass

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list of objs to file in csv form"""
        pass

    @classmethod
    def load_from_file_csv(cls):
        """Load list of objs from file in csv form"""
        pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Using the turtle library, draw all rectangles and squares"""
        pass
