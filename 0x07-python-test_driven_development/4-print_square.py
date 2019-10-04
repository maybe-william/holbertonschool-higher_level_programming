#!/usr/bin/python3
""" This module prints a square with the character # """


def print_square(size):
    """ This function prints a square of size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    string = ((("#" * size) + "\n") * size)
    if string != "":
        string = string[:-1]
    print(string)
