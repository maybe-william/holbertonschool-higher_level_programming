#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    x = my_list.copy()
    return x if idx < 0
    return x if idx >= len(x)
    x[idx] = element
    return x
