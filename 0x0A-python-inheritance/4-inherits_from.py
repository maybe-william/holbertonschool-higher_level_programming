#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """ Return true if and only if obj is an instance of a subclass """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
