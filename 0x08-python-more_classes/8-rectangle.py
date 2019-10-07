#!/usr/bin/python3
""" This module defines a rectangle. """


class Rectangle:
    """ A rectangle """

    number_of_instances = 0
    """ the number of rectangle instances in existence """

    print_symbol = '#'
    """ the print symbol"""

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the larger of two rectangles by area """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def __verify_int(self, value, tp):
        """ Verify an int """
        if type(value) is not int:
            raise TypeError(tp + ' must be an integer')
        if value < 0:
            raise ValueError(tp + ' must be >= 0')

    def __str__(self):
        """ Return a string representation """
        rect = (((str(self.print_symbol) * self.width) + '\n') * self.height)
        if rect == '' or rect == '\n' * self.height:
            return ''
        return rect[:-1]

    def __repr__(self):
        """ Return an evalable rectangle representation """
        ret = 'Rectangle({:d}, {:d})'.format(self.width, self.height)
        return ret

    def __del__(self):
        """ Detect object deletion """
        print('Bye rectangle...')
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    def __init__(self, width=0, height=0):
        """ Create a rectangle """
        self.__verify_int(width, 'width')
        self.__width = width
        self.__verify_int(height, 'height')
        self.__height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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
