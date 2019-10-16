#!/usr/bin/python3
""" module: student2 """


class Student:
    """ The student class """

    def __init__(self, first_name, last_name, age):
        """ Init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dict representation of attributes """
        t = type(attrs)
        if t is list and len(attrs) > 0 and type(attrs[0]) is str:
            return {k: v for k, v in vars(self).items() if k in attrs}
        return vars(self)

    def reload_from_json(self, json):
        """ Reload the state of self from json """
        for k, v in json.items():
            setattr(self, k, v)
