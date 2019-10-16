#!/usr/bin/python3
""" module: load, add, save """
import json
import sys


if __name__ == '__main__':
    load = __import__('8-load_from_json_file').load_from_json_file
    save = __import__('7-save_to_json_file').save_to_json_file
    exists = True
    with open("add_item.json", "a+") as f:
        if f.tell() == 0:
            exists = False
    l = load("add_item.json") if exists else []
    extra = sys.argv[1:]
    l = l + extra
    save(l, "add_item.json")
