#!/usr/bin/python3
# comment
"""module: models"""
import json
import turtle


class Base:
    """class: Base"""

    __nb_objects = 0
    """The number of instances extending this"""

    def __init__(self, id=None):
        """Init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of cls with attributes already set"""
        if cls.__name__ == "Rectangle":
            x = cls(1, 1, 1, 1)
        elif cls.__name__ == "Square":
            x = cls(1, 1, 1)
        else:
            return None
        x.update(**dictionary)
        return x

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a json string representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries represented by a json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of objs to file in json form"""
        j = Base.to_json_string([x.to_dictionary() for x in list_objs])
        with open(cls.__name__ + ".json", "w+") as f:
            f.write(j)

    @classmethod
    def load_from_file(cls):
        """Load list of objs from file in json form"""
        with open(cls.__name__ + ".json", "r+") as f:
            j = f.readlines()
        dicts = Base.from_json_string("".join(j))
        return list(map(lambda x: (cls.create(**x)), dicts))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list of objs to file in csv form"""
        if cls.__name__ == "Rectangle":
            attrs = [[x.id, x.width, x.height, x.x, x.y] for x in list_objs]
        elif cls.__name__ == "Square":
            attrs = [[x.id, x.size, x.x, x.y] for x in list_objs]
        else:
            return
        attrs = list(map(lambda x: (list(map(str, x))), attrs))
        with open(cls.__name__ + ".csv", "w+") as f:
            for dat in attrs:
                f.write(",".join(dat) + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """Load list of objs from file in csv form"""
        with open(cls.__name__ + ".csv", "r+") as f:
            dats = f.readlines()
        objs = []
        for dat in dats:
            d = dat.rstrip().split(",")
            d = list(map(int, d))
            x = cls.create()
            x.update(*d)
            objs.append(x)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Using the turtle library, draw all rectangles and squares"""
        turtle.Screen()
        turtle.speed(10)
        tot = list_rectangles + list_squares
        for obj in tot:
            p1 = (obj.x, obj.y)
            p2 = (obj.x + obj.width, obj.y)
            p3 = (obj.x + obj.width, obj.y + obj.height)
            p4 = (obj.x, obj.y + obj.height)
            turtle.up()
            turtle.setpos(p1)
            turtle.down()
            turtle.setpos(p2)
            turtle.setpos(p3)
            turtle.setpos(p4)
            turtle.setpos(p1)
