#!/usr/bin/python3
""" module: append to a file """


def append_write(filename="", text=""):
    """ append text to a file and return bytes written """
    if filename == "":
        return 0
    with open(filename, "a+") as f:
        return f.write(text)
