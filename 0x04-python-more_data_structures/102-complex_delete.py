#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    ad = a_dictionary.copy()
    for i in ad.items():
        if i[1] == value:
            a_dictionary.pop(i[0], None)
    return a_dictionary
