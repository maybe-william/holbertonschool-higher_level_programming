#!/usr/bin/python3
"""Find a peak in a list of integers"""


def find_peak(list_of_integers):
    """Find a peak in a list of integers"""
    if list_of_integers is None:
        return None
    if list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    last = False
    for x in list_of_integers:
        if last and x < last:
            return x
        last = x
    return last
