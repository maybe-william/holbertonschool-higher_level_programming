#!/usr/bin/python3
""" module: search and update """


def readstuff(filename=""):
    """ read lines and return """
    if filename == "":
        return
    with open(filename, "r") as f:
        x = f.readlines()
        return x

def append_after(filename="", search_string="", new_string=""):
    """ Append new_string after line with search string """
    x = readstuff(filename)
    y = []
    for i in x:
        y.append(i)
        if search_string in i:
            y.append(new_string)
    with open(filename, "w") as f:
        for j in y:
            f.write(j)
