#!/usr/bin/python3
"""0-square

Define a square

"""


class square:
    """A square

    Represent a square

    """

    __size = None

    def __verify_int(i):
        """verify int method

        Verify int and >= 0

        Args:
            i: the int

        Raises:
            TypeError
            ValueError

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        """init method

        Initialize a square

        Args:
            size (int): the size of the square

        Raises:
            TypeError
            ValueError

        """
        __verify_int(size)
        self.__size = size

    def size(self):
        """size getter

        Give the size

        Returns:
            the size

        Raises:
            TypeError
            ValueError

        """

        __verify_int(self.__size)
        return self.__size

    def size(self, value):
        """size setter

        Set the size

        Args:
            value: the value to set

        Raises:
            TypeError
            ValueError

        """

        __verify_int(value)
        self.__size = value

    def area(self):
        """area method

        Get the area

        Returns:
            the area

        """

        return self.__size * self.__size
