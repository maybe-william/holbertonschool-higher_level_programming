#!/usr/bin/python3
""" Create MyList class """


class MyList(list):
    """ MyList class inherits from list """

    def print_sorted(self):
        """ Prints the sorted list """
        print(sorted(self))
