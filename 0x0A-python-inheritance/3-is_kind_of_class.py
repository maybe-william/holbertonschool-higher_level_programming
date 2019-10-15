#!/usr/bin/python3
""" Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """ Return true if obj is a class or subclass """
    if isinstance(obj, a_class):
        return True
    return False
