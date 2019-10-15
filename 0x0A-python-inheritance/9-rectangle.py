#!/usr/bin/python3
""" Full rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The rectangle class """

    def __init__(self, width, height):
        """ Init """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Get the area """
        return self.__width * self.__height

    def __str__(self):
        """ Create a string representation to be printed """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
