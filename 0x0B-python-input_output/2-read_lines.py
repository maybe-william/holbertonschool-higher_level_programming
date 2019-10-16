#!/usr/bin/python3
""" module: read n lines """


def read_lines(filename="", nb_lines=0):
    """ read nb_lines and print """
    if filename == "":
        return
    if nb_lines <= 0:
        with open(filename, "r") as f:
            x = f.readlines()
    else:
        with open(filename, "r") as f:
            x = []
            for i in range(0, nb_lines):
                x.append(f.readline())
    for i in x:
        print(i, end="")
