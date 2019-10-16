#!/usr/bin/python3
""" module: from JSON """
import json


def from_json_string(my_str):
    """ deserialize an object """
    return json.loads(my_str)
