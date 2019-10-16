#!/usr/bin/python3
""" module: to JSON file """
import json


def save_to_json_file(my_obj, filename):
    """ serialize an object into a file """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
