#!/usr/bin/python3
# comment
"""module: models"""
import models.base
Base = models.base.Base


class Rectangle (Base):
    """class: Rectangle"""

    def val_int(self, name, val, vs=">"):
        """Validate an int and throw an error if something's wrong"""
        if type(val) is not int:
            raise TypeError("{} must be an integer".format(name))
        if vs == ">" and val <= 0:
            raise ValueError("{} must be {} 0".format(name, vs))
        if vs == ">=" and val < 0:
            raise ValueError("{} must be {} 0".format(name, vs))

    def __str__(self):
        """Return a str representation of the object"""
        name = "[Rectangle]"
        dat = " ({}) {}/{}".format(self.id, self.x, self.y)
        dat2 = " - {}/{}".format(self.width, self.height)
        return name + dat + dat2

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        self.val_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        self.val_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Get height"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set height"""
        self.val_int("x", value, ">=")
        self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        self.val_int("y", value, ">=")
        self.__y = value

    def area(self):
        """Return the area"""
        return self.width * self.height

    def to_dictionary(self):
        """Return the dictionary representation of this object"""
        tmp = {}
        x = vars(self)
        for k, v in x.items():
            tmp[k.split('__')[-1]] = v
        return tmp

    def update(self, *args, **kwargs):
        """Update the attributes of this object"""
        if args is not None and args != ():
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def display(self):
        """Print a representation of this object to stdout"""
        rep = ""
        front = (" " * self.x)
        rep = rep + ("\n" * self.y)
        line = ("#" * self.width) + "\n"

        rep = rep + ((front + line) * self.height)
        print(rep, end="")
