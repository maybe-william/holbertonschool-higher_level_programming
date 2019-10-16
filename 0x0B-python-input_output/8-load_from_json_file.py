#!/usr/bin/python3
""" module: from a JSON file """
import json


def load_from_json_file(filename):
    """ deserialize an object from a file """
    with open(filename, "r") as f:
        return json.load(f)
