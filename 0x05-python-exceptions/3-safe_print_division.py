#!/usr/bin/python3


def safe_print_division(a, b):
    """Print a / b with exception handling"""
    try:
        val = a / b
    except ZeroDivisionError:
        val = None
    finally:
        print("Inside result: {}".format(val))
        return val
