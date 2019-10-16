#!/usr/bin/python3
""" module: number of lines """


def number_of_lines(filename=""):
    """ count the number of lines of a file """
    n = 0
    if filename == "":
        return n
    with open(filename, "r") as f:
        for line in f:
            n = n + 1
    return n
