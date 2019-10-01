#!/usr/bin/python3
"""0-square

Define a square

"""


class square:
    """A square

    Represent a square

    """

    __size = None

    def __init__(self, size=0):
        """init method

        Initialize a square

        Args:
            size (int): the size of the square

        Raises:
            TypeError
            ValueError

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area method

        Give the area

        Returns:
            the area

        """

        return self.__size * self.__size
