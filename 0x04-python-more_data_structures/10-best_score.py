#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mymax = (None, 0)
    for i in a_dictionary.items():
        if i[1] > mymax[1]:
            mymax = i
    return mymax[0]
