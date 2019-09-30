#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Print an integer with exception handling"""
    res = None
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: " + e.__str__(), file=sys.stderr)
    return res
