#!/usr/bin/python3
"""module: test_models"""
import unittest


class TestBase(unittest.TestCase):
    """class: TestBase"""

    m = "Not implemented"

    @classmethod
    def setUpClass(cls):
        """Set up class tests"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Tear down class tests"""
        pass

    def test_init(self):
        """Test init works"""
        fail(m)
    
    def test_nbobjs(self):
        """Test nb_objs works"""
        fail(m)

    def test_valint(self):
        """Test val_int works"""
        fail(m)

    def test_create(self):
        """Test create works"""
        fail(m)

    def test_tojson(self):
        """Test to_json_string works"""
        fail(m)

    def test_fromjson(self):
        """Test from_json_string works"""
        fail(m)

    def test_save(self):
        """Test save_to_file works"""
        fail(m)

    def test_load(self):
        """Test load_from_file works"""
        fail(m)

    def test_savecsv(self):
        """Test save_to_file_csv works"""
        fail(m)

    def test_loadcsv(self):
        """Test load_from_file_csv works"""
        fail(m)
