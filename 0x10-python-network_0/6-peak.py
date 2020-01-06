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

    dir1 = False
    dir2 = False
    max_peak = False
    for i in range(len(list_of_integers)):
        if i == 0:
            continue
        else:
            dir1 = dir2
            x = list_of_integers[i - 1]
            y = list_of_integers[i]
            if x < y:
                dir2 = 1
            elif y < x:
                dir2 = -1
            else:
                dir2 = 0

            if i == 1:
                continue

            if dir1 > 0 and dir2 < 0:
                if (not max_peak) or (x > max_peak):
                    max_peak = x
                    return x
    if (not max_peak):
        x = list_of_integers[0]
        y = list_of_integers[-1]
        if x > y:
            max_peak = x
        else:
            max_peak = y

    return max_peak
