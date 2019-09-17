#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print()
        return
    x = my_list.copy()
    x.reverse()
    for i in x:
        print("{:d}".format(i))
