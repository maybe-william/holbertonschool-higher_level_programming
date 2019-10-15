#!/usr/bin/python3
""" Can I """


def add_attribute(obj, name, thing):
    """ Add an attribute to an object if it doesn't have it """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.name = thing
