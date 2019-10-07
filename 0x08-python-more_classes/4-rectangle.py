#!/usr/bin/python3
""" This module defines a rectangle. """


class Rectangle:
    """ A rectangle """

    def __verify_int(self, value, tp):
        """ Verify an int """
        if type(value) is not int:
            raise TypeError(tp + ' must be an integer')
        if value < 0:
            raise ValueError(tp + ' must be >= 0')

    def __str__(self):
        """ Return a string representation """
        rect = ((('#' * self.width) + '\n') * self.height)
        if rect == '' or rect == '\n' * self.height:
            return ''
        return rect[:-1]

    def __repr__(self):
        """ Return an evalable rectangle representation """
        ret = 'Rectangle({:d}, {:d})'.format(self.width, self.height)
        return ret

    def __init__(self, width=0, height=0):
        """ Create a rectangle """
        self.__verify_int(width, 'width')
        self.__width = width
        self.__verify_int(height, 'height')
        self.__height = height

    @property
    def width(self):
        """ Get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width """
        self.__verify_int(value, 'width')
        self.__width = value

    @property
    def height(self):
        """ Get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height """
        self.__verify_int(value, 'height')
        self.__height = value

    def area(self):
        """ Return the area """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        """ Return the perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height
