#!/usr/bin/python3
""" This module uses urllib to make a request """

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        d = ""
    else:
        d = sys.argv[1]
    resp = requests.get("https://swapi.co/api/people/", params={'search': d})
    if resp.status_code == 204 or resp.json() == {}:
        print('No result')
    else:
        try:
            j = resp.json()
            print("Number of results: {}".format(j.get('count', 0)))
            for i in j.get('results', []):
                print(i.get('name', ""))
        except:
            print('Not a valid JSON')
