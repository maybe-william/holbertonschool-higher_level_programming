#!/usr/bin/python3
""" This module uses urllib to make a request """

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        datum = ""
    else:
        datum = sys.argv[1]
    resp = requests.post("http://0.0.0.0:5000/search_user", data={'q': datum})
    if resp.status_code == 204 or resp.json() == {}:
        print('No result')
    else:
        try:
            j = resp.json()
            print("[{}] {}".format(j.get('id', ''), j.get('name', '')))
        except:
            print('Not a valid JSON')
