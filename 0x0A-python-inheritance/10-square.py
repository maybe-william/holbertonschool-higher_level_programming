#!/usr/bin/python3
""" Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The square class """

    def __init__(self, size):
        """ Init """
        super().__init__(size, size)
        self.__size = size
