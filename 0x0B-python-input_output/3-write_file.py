#!/usr/bin/python3
""" module: write to a file """


def write_file(filename="", text=""):
    """ write text to a file and return bytes written """
    if filename == "":
        return 0
    with open(filename, "w+") as f:
        return f.write(text)
