#!/usr/bin/python3
""" This module uses urllib to make a request """

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        html = resp.headers["X-Request-Id"]
        print(html)
