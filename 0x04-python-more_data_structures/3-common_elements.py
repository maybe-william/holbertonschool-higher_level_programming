#!/usr/bin/python3


def common_elements(set_1, set_2):
    if set_1 is None:
        set_1 = {}
    if set_2 is None:
        set_2 = {}
    return set_1.intersection(set_2)
