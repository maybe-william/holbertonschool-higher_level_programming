#!/usr/bin/python3
"""module: models"""


class Square (Rectangle):
    """class: Square"""

    def __str__(self):
        """Return a str representation of this object"""
        start = super().__str__()
        mid = start.split("]")[-1]
        mid = mid.split("-")[0]
        return "[Square]" + mid + "- {}".format(self.size)

    def __init__(self, size, x=0, y=0, id=None):
        """Init"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size"""
        return self.width()

    @size.setter
    def size(self, value):
        """Set size"""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return the dictionary representation of this object"""
        return vars(self)

    def update(self, *args, **kwargs):
        """Update the attributes of this object"""
        if args is not None and args != []:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        elif kwargs is not None and args != {}:
            for k, v in kwargs.items():
                setattr(self, k, v)
