#!/usr/bin/python3
""" This module uses urllib to make a request """

import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    resp = requests.get("https://api.github.com/user",
                        auth=HTTPBasicAuth(u, p))
    if resp.status_code == 204 or resp.json() == {}:
        print('No result')
    else:
        try:
            j = resp.json()
            print(j.get('id', None))
        except:
            print('Not a valid JSON')
