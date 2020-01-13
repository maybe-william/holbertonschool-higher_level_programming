#!/usr/bin/python3
"""Get the number of commits using the github api"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    own = sys.argv[1] + '/'
    repo = sys.argv[2] + '/'
    comm = 'commits'
    resp = requests.get('https://api.github.com/repos/' + own + repo + comm)
    j = resp.json()
    limit = len(j)
    if limit > 10:
        limit = 10
    if type(j) != list and j.get('message', '') == 'Not Found':
        exit()
    for i in j[:limit]:
        print(i['sha'] + ': ' + i['commit']['committer']['name'])
