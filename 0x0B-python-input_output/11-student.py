#!/usr/bin/python3
""" module: student1 """


class Student:
    """ The student class """

    def __init__(self, first_name, last_name, age):
        """ Init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns a dict representation of attributes """
        return vars(self)
