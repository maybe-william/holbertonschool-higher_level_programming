#!/usr/bin/python3


def uniq_add(my_list=[]):
    if my_list is None:
        return None
    z = 0
    for x in set(my_list):
        z = z + x
    return z
