#!/usr/bin/python3
""" Square """


class Square(Rectangle):
    """ The square class """

    def __init__(self, size):
        """ Init """
        self.__size = size
        Rectangle(size, size)
