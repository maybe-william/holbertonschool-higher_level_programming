#!/usr/bin/python3
""" Make a locked class """


class LockedClass:
    """ The locked class """

    def __init__(self):
        """ Init """
        self.first_name = None

    def __setattr__(self, name, value):
        """ Set an attr. This should be locked down """
        if name != 'first_name':
            second = "no attribute '" + name + "'"
            raise AttributeError("'LockedClass' object has " + second)
        self.__dict__['first_name'] = value
