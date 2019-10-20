#!/usr/bin/python3
"""module: models"""


class Rectangle (Base):
    """class: Rectangle"""

    def __str__(self):
        """Return a str representation of the object"""
        pass

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init"""
        pass

    @property
    def width(self):
        """Get width"""
        pass

    @width.setter
    def width(self, value):
        """Set width"""
        pass

    @property
    def height(self):
        """Get height"""
        pass

    @height.setter
    def height(self, value):
        """Set height"""
        pass

    @property
    def x(self):
        """Get height"""
        pass

    @x.setter
    def x(self, value):
        """Set height"""
        pass

    @property
    def y(self):
        """Get y"""
        pass

    @y.setter
    def y(self, value):
        """Set y"""
        pass

    def area(self):
        """Return the area"""
        pass

    def to_dictionary(self):
        """Return the dictionary representation of this object"""
        pass

    def update(self, *args, **kwargs):
        """Update the attributes of this object"""
        pass

    def display(self):
        """Print a representation of this object to stdout"""
        pass
