#!/usr/bin/python3
"""Define a square"""


class Square:
    """A square"""

    __size = None
    __position = None

    def __verify_tuple(t):
        """Verify t is two ints not less than 0"""

        err = TypeError("position must be a tuple of 2 positive integers")

        if type(t) != tuple:
            raise err
        if len(t) != 2:
            raise err
        if type(t[0]) != int or type(t[1]) != int:
            raise err
        if t[0] < 0 or t[1] < 0:
            raise err

    def __verify_int(i):
        """Verify i is int and >= 0"""

        if type(i) != int:
            raise TypeError("size must be an integer")
        if i < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square"""
        Square.__verify_int(size)
        self.__size = size
        Square.__verify_tuple(position)
        self.__position = position

    def __str__(self):
        """Make a string representation"""
        string = ""
        if self.__size == 0:
            return ""
        for x in range(0, self.__position[1]):
            string = string + "\n"
        for i in range(0, self.__size):
            string = string + (" " * self.__position[0])
            string = string + ("#" * self.__size)
            string = string + "\n"
        return string[:-1]

    @property
    def size(self):
        """Give the size"""

        Square.__verify_int(self.__size)
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""

        Square.__verify_int(value)
        self.__size = value

    @property
    def position(self):
        """Get the position"""

        Square.__verify_tuple(self.__position)
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position"""

        Square.__verify_tuple(value)
        self.__position = value

    def area(self):
        """Get the area"""

        return self.__size * self.__size

    def my_print(self):
        """Print the square to stdout"""
        print(self)
