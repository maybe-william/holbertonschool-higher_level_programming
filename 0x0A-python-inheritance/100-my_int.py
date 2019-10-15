#!/usr/bin/python3
""" My integer """


class MyInt(int):
    """ My integer """

    def __eq__(self, other):
        """ not equal """
        return super().__ne__(other)

    def __ne__(self, other):
        """ equal """
        return super().__eq__(other)
