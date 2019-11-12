#!/usr/bin/python3
""" unit test for max int [] """
import unittest
m2 = __import__('6-max_integer')
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This class tests the max_integer function """

    @classmethod
    def setUpClass(cls):
        """ class setup """
        with open(m2.__file__, "r") as f:
            if "Modules" in f.read():
                cls.err = True
            else:
                cls.err = False

    def test_empty(self):
        """ test empty list """
        if not type(self).err:
            self.assertEqual(1, 0)
        self.assertIs(max_integer([]), None)

    def test_end(self):
        """ test empty list """
        if not type(self).err:
            self.assertEqual(1, 0)
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_beginning(self):
        """ test empty list """
        if not type(self).err:
            self.assertEqual(1, 0)
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_middle(self):
        """ test empty list """
        if not type(self).err:
            self.assertEqual(1, 0)
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_negative(self):
        """ test empty list """
        if not type(self).err:
            self.assertEqual(1, 0)
        self.assertEqual(max_integer([2, 3, -4]), 3)

    def test_all_negative(self):
        """ test empty list """
        if not type(self).err:
            self.assertEqual(1, 0)
        self.assertEqual(max_integer([-2, -3, -4]), -2)

    def test_samelist(self):
        """ test same list """
        if not type(self).err:
            self.assertEqual(1, 0)
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_oneitem(self):
        """ test a list with only one item """
        if not type(self).err:
            self.assertEqual(1, 0)
        self.assertEqual(max_integer([3]), 3)

    def test_noargs(self):
        """ test no list """
        if not type(self).err:
            self.assertEqual(1, 0)
        self.assertIs(max_integer(), None)
