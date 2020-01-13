#!/usr/bin/python3
""" This module uses urllib to make a request """

import requests
import sys


if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    html = resp.headers.get("X-Request-Id", None)
    print(html)
