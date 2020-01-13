#!/usr/bin/python3
""" This module uses urllib to make a request """

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = {}
    data['email'] = sys.argv[2]
    url_end = urllib.parse.urlencode(data)
    url_end = url_end.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], url_end) as resp:
        html = resp.read()
        print(str(html, 'utf-8'))
