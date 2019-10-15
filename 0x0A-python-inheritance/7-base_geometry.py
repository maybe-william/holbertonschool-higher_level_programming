#!/usr/bin/python3
""" Integer validator """


class BaseGeometry():
    """ The base geometry class """

    def integer_validator(self, name, value):
        """ Validate an integer """
        if type(value) is not int:
            raise TypeError(str(name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")

    def area(self):
        """ Give the area """
        raise Exception("area() is not implemented")
