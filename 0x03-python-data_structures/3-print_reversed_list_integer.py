#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    x = my_list.copy()
    x.reverse()
    for i in x:
        print("{:d}".format(i))
