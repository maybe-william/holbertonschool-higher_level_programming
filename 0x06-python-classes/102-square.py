#!/usr/bin/python3
"""Define a square"""


class Square:
    """A square"""

    __size = None

    def __verify_int(i):
        """Verify i is int and >= 0"""

        if type(i) != int:
            raise TypeError("size must be an integer")
        if i < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        """Initialize a square"""
        Square.__verify_int(size)
        self.__size = size

    def __lt__(self, other):
        """Comparison operator <"""
        return type(other) == Square and self.size < other.size

    def __le__(self, other):
        """Comparison operator <="""
        return type(other) == Square and self.size <= other.size

    def __gt__(self, other):
        """Comparison operator >"""
        return type(other) == Square and self.size > other.size

    def __ge__(self, other):
        """Comparison operator >="""
        return type(other) == Square and self.size >= other.size

    def __eq__(self, other):
        """Comparison operator =="""
        return type(other) == Square and self.size == other.size

    def __ne__(self, other):
        """Comparison operator !="""
        return type(other) == Square and self.size != other.size

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

    def area(self):
        """Get the area"""

        return self.__size * self.__size
