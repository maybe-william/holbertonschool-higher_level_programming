#!/usr/bin/python3


def no_c(my_string):
    x = list(my_string)
    y = "".join([z for z in x if z != "c" and z != "C"])
    return y
