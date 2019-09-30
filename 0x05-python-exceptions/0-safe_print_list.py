#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Print a list with exception handling"""
    if x == 0:
        return 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except:
            print()
            return i + 1
    print()
    return x
