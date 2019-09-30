#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer with exception handling"""
    try:
        print("{:d}".format(value))
    except:
        return False
    return True
