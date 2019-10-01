#!/usr/bin/python3
"""0-square

Define a square

"""


class square:
    """A square

    Represent a square

    """

    __size = None
    __position = None

    def __verify_tuple(t):
        """verify tuple method

        Verify t is two ints not less than 0

        Args:
            t: the tuple

        Raises:
            TypeError

        """

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

    def __init__(self, size=0, position=(0, 0)):
        """init method

        Initialize a square

        Args:
            size: the size of the square
            position: the x, y position of the square

        Raises:
            TypeError
            ValueError

        """
        __verify_int(size)
        self.__size = size
        __verify_tuple(position)
        self.__position = position

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

    def position(self):
        """position getter

        Get the position

        Returns:
            the position

        Raises:
            TypeError

        """

        __verify_tuple(self.__position)
        return self.__position

    def position(self, value):
        """position setter

        Set the position

        Args:
            value: the value to set

        Raises:
            TypeError

        """

        __verify_tuple(value)
        self.__position = value

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
        for x in range(0, self.__position[0]):
            print()
        for i in range(0, self.__size):
            print((" " * self.__position[1]) + ("#" * self.__size))
