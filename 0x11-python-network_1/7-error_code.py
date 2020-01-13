#!/usr/bin/python3
""" This module uses urllib to make a request """

import requests
import sys


if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
