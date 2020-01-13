#!/usr/bin/python3
""" This module uses urllib to make a request """

import requests
import sys


def print_char(char_json):
    """print the character data"""
    print(char_json.get("name", ""))
    for i in char_json['films']:
        resp = requests.get(i)
        print("\t{}".format(resp.json()['title']))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        d = ""
    else:
        d = sys.argv[1]
    resp = requests.get("https://swapi.co/api/people/", params={'search': d})
    if resp.status_code == 204 or resp.json() == {}:
        print('No result')
    else:
        j = resp.json()
        print("Number of results: {}".format(j.get('count', 0)))
        peeps = j.get('results', [])
        while peeps != []:
            for i in peeps:
                print_char(i)
            if j.get('next', False):
                j = requests.get(j['next']).json()
                peeps = j.get('results', [])
            else:
                peeps = []
