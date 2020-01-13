#!/usr/bin/python3
""" This module uses urllib to make a request """

import requests
import sys


if __name__ == "__main__":
    resp = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(resp.text)
