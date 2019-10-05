#!/usr/bin/python3
""" unit test for max int [] """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This class tests the max_integer function """

    def test_empty(self):
        """ test empty list """
        self.assertIs(max_integer([]), None)

    def test_nonlist(self):
        """ test not list type """
        self.assertRaises(TypeError, max_integer, ["aasdf"])

    def test_samelist(self):
        """ test same list """
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_notallints(self):
        """ test list with not all ints """
        self.assertRaises(TypeError, max_integer, [[3, 4, "5"]])

    def test_oneitem(self):
        """ test a list with only one item """
        self.assertEqual(max_integer([3]), 3)

    def test_noargs(self):
        """ test no list """
        self.assertIs(max_integer(), None)
