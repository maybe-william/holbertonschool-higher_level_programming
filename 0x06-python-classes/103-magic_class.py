#!/usr/bin/python3
"""This gets disassembled into goodness"""
import math


class MagicClass:
    """Magic class"""

    def __init__(self, radius):
        """init method"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area method"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """circumference method"""
        return (2 * math.pi * self.__radius)
