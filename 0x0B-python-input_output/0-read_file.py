#!/usr/bin/python3
""" module: read file """


def read_file(filename=""):
    """ read a file and print it to stdout """
    if filename == "":
        return
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")
