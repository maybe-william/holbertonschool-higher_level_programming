#!/usr/bin/python3
""" This module uses urllib to make a request """

import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            html = resp.read()
            print(str(html, 'utf-8'))
    except urllib.error.HTTPError as h:
        print('Error code: {}'.format(h.code))
