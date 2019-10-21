#!/usr/bin/python3
"""module: test_models"""
import unittest
import os
import models.base
import models.rectangle
import models.square
Base = models.base.Base
Rectangle = models.rectangle.Rectangle
Square = models.square.Square


class TestBase(unittest.TestCase):
    """class: TestBase"""

    @classmethod
    def setUpClass(cls):
        """Set up class tests"""
        cls.m = "Not implemented"
        cls.one = Base()
        cls.two = Base(43)
        cls.three = Base()
        cls.rone = Rectangle(1, 1)
        cls.rtwo = Rectangle(2, 4, 2, 1, 35)
        try:
            cls.rthree = Rectangle(-1, 0)
        except:
            pass
        cls.rfour = Rectangle(10, 20, 0, 0)
        cls.sone = Square(5, 0, 3)
        cls.stwo = Square(3, 0, 4, 90)

    def setUp(self):
        """Set up before each test"""
        self.ae = self.assertEqual
        self.ar = self.assertRaises

    @classmethod
    def tearDownClass(cls):
        """Tear down class tests"""
        pass

    def test_init(self):
        """Test init works"""
        self.ae(self.rone.width, 1)
        self.ae(self.rone.height, 1)
        self.ae(self.rone.x, 0)
        self.ae(self.rone.y, 0)

        self.ae(self.rtwo.width, 2)
        self.ae(self.rtwo.height, 4)
        self.ae(self.rtwo.x, 2)
        self.ae(self.rtwo.y, 1)

        self.ae(hasattr(self, "rthree"), False)

        self.ae(self.sone.size, 5)
        self.ae(self.sone.width, 5)
        self.ae(self.sone.height, 5)
        self.ae(self.sone.x, 0)
        self.ae(self.sone.y, 3)

        self.ae(self.stwo.size, 3)
        self.ae(self.stwo.width, 3)
        self.ae(self.stwo.height, 3)
        self.ae(self.stwo.x, 0)
        self.ae(self.stwo.y, 4)

    def test_nbobjs(self):
        """Test nb_objs works"""
        self.ae(self.one.id, 1)
        self.ae(self.two.id, 43)
        self.ae(self.three.id, 2)
        self.ae(self.rone.id, 3)
        self.ae(self.rtwo.id, 35)
        self.ae(self.rfour.id, 4)
        self.ae(self.sone.id, 5)
        self.ae(self.stwo.id, 90)

    def test_valint(self):
        """Test val_int works"""
        with self.ar(ValueError):
            self.rone.width = 0
        with self.ar(ValueError):
            self.rone.height = 0
        with self.ar(ValueError):
            self.rone.x = -1
        with self.ar(ValueError):
            self.rone.y = -1

        with self.ar(ValueError):
            self.rone.width = -1
        with self.ar(ValueError):
            self.rone.height = -1

        with self.ar(ValueError):
            self.stwo.size = 0
        with self.ar(ValueError):
            self.stwo.height = 0
        with self.ar(ValueError):
            self.stwo.width = 0
        with self.ar(ValueError):
            self.stwo.x = -2
        with self.ar(ValueError):
            self.stwo.y = -5

        with self.ar(ValueError):
            self.stwo.size = -1
        with self.ar(ValueError):
            self.stwo.width = -1
        with self.ar(ValueError):
            self.stwo.height = -3

        with self.ar(TypeError):
            self.rone.width = "purp"
        with self.ar(TypeError):
            self.rone.height = "gree"
        with self.ar(TypeError):
            self.rone.x = "rose"
        with self.ar(TypeError):
            self.rone.y = "red"

        with self.ar(TypeError):
            self.sone.size = "pink"
        with self.ar(TypeError):
            self.sone.height = "puce"
        with self.ar(TypeError):
            self.sone.width = "aqua"
        with self.ar(TypeError):
            self.sone.x = "grep"
        with self.ar(TypeError):
            self.sone.y = "x"

    def test_create(self):
        """Test create works"""
        sd = {"size": 5, "x": 4, "y": 6, "id": 50}
        rd = {"width": 5, "height": 2, "x": 0, "y": 1, "id": 30}
        x = Base.create()
        y = Rectangle.create(**rd)
        z = Square.create(**sd)

        self.ae(x, None)

        self.ae(y.width, 5)
        self.ae(y.height, 2)
        self.ae(y.x, 0)
        self.ae(y.y, 1)
        self.ae(y.id, 30)

        self.ae(z.size, 5)
        self.ae(z.width, 5)
        self.ae(z.height, 5)
        self.ae(z.x, 4)
        self.ae(z.y, 6)
        self.ae(z.id, 50)

    def test_tojson(self):
        """Test to_json_string works"""
        ld = [{"a": "x"}, {"b": "y"}, {"c": "z"}, {}]
        res = '[{"a": "x"}, {"b": "y"}, {"c": "z"}, {}]'
        self.ae(Base.to_json_string(ld), res)

        self.ae(Base.to_json_string([]), "[]")
        self.ae(Base.to_json_string(None), "[]")

    def test_fromjson(self):
        """Test from_json_string works"""
        self.ae(Base.from_json_string(None), [])
        self.ae(Base.from_json_string(""), [])
        self.ae(Base.from_json_string('[{"a": "z"}]'), [{"a": "z"}])

    def test_save_and_load(self):
        """Test save_to_file and load_from_file work"""
        rect = {"width": 5, "height": 3, "x": 2, "y": 1, "id": 20}
        myr = Rectangle.create(**rect)
        Rectangle.save_to_file([myr, myr])
        myr.width = myr.width - 1
        twor = Rectangle.load_from_file()

        self.ae(twor[0].width, myr.width + 1)

        sq = {"size": 10, "x": 1, "y": 2, "id": 30}
        mys = Square.create(**sq)
        Square.save_to_file([mys, mys])
        mys.size = mys.size - 1
        twos = Square.load_from_file()

        self.ae(twos[0].size, mys.size + 1)
        os.remove("Rectangle.json")
        os.remove("Square.json")

    def test_savecsv_and_loadcsv(self):
        """Test save_to_file_csv and load_from_file_csv work"""
        rect = {"width": 5, "height": 3, "x": 2, "y": 1, "id": 20}
        myr = Rectangle.create(**rect)
        Rectangle.save_to_file_csv([myr, myr])
        myr.width = myr.width - 1
        twor = Rectangle.load_from_file_csv()

        self.ae(twor[0].width, myr.width + 1)

        sq = {"size": 10, "x": 1, "y": 2, "id": 30}
        mys = Square.create(**sq)
        Square.save_to_file_csv([mys, mys])
        mys.size = mys.size - 1
        twos = Square.load_from_file_csv()

        self.ae(twos[0].size, mys.size + 1)
        os.remove("Rectangle.csv")
        os.remove("Square.csv")

    def test_str(self):
        """Test __str__ works"""
        self.ae(str(self.rone), "[Rectangle] (3) 0/0 - 1/1")
        self.ae(str(self.rtwo), "[Rectangle] (35) 2/1 - 2/4")
        self.ae(str(self.rfour), "[Rectangle] (4) 0/0 - 10/20")
        self.ae(str(self.sone), "[Square] (5) 0/3 - 5")
        self.ae(str(self.stwo), "[Square] (90) 0/4 - 3")

    def test_area(self):
        """Test area works"""
        self.ae(self.rone.area(), 1)
        self.ae(self.rtwo.area(), 8)
        self.ae(self.rfour.area(), 200)
        self.ae(self.sone.area(), 25)
        self.ae(self.stwo.area(), 9)
