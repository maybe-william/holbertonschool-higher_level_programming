#!/usr/bin/python3
"""0-square

Define a square

"""


class Square:
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

        if type(i) != int:
            raise TypeError("size must be an integer")
        if i < 0:
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
        Square.__verify_int(size)
        self.__size = size

    @property
    def size(self):
        """size getter

        Give the size

        Returns:
            the size

        Raises:
            TypeError
            ValueError

        """

        Square.__verify_int(self.__size)
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

        Set the size

        Args:
            value: the value to set

        Raises:
            TypeError
            ValueError

        """

        Square.__verify_int(value)
        self.__size = value

    def area(self):
        """area method

        Get the area

        Returns:
            the area

        """

        return self.__size * self.__size

    def my_print(self):
        """printing method

        Print the square to stdout

        """

        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            print("#" * self.__size)
