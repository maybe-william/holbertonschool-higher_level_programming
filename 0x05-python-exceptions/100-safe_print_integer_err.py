#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Print an integer with exception handling"""
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: " + e.__str__(), file=sys.stderr)
        return False
    return True
