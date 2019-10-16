#!/usr/bin/python3
""" module: to JSON """
import json


def to_json_string(my_obj):
    """ serialize an object """
    return json.dumps(my_obj)
