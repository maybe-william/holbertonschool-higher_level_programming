#!/usr/bin/python3
""" module: class to json """


def class_to_json(obj):
    """ return a dictionary description for a json """
    return vars(obj)
