#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Print a list of integers with exception handling"""
    tot = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            tot = tot + 1
        except:
            pass
    print()
    return tot
