#!/usr/bin/python3
""" Integer validator """


class Rectangle(BaseGeometry):
    """ The rectangle class """

    def __init__(self, width, height):
        """ Init """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
