#!/usr/bin/python3


def max_integer(my_list=[]):
    return None if len(my_list) == 0
    max = my_list[0]
    for x in my_list:
        max = x if x > max
    return x
