#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    k = sorted(a_dictionary.keys())
    for i in k:
        print(i + ": " + str(a_dictionary.get(i)))
