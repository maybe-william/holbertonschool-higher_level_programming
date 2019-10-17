#!/usr/bin/python3
""" module: log parsing """
import sys


class Dat:
    """ class to hold data """
    filesizes = [0]
    status = {}


def printLog():
    """ Print one log """
    size = sum(Dat.filesizes)
    print("File size: {}".format(size))
    x = sorted(Dat.status.keys())
    for k in x:
        print(str(k) + ": " + str(Dat.status[k]))


count = 0
try:
    for i in sys.stdin:
        if count == 10:
            printLog()
            count = 0
        fsize = int(i.split(' ')[-1].rstrip())
        Dat.filesizes.append(fsize)
        code = int(i.split(' ')[-2])
        Dat.status[code] = Dat.status.get(code, 0) + 1
        count = count + 1
except (KeyboardInterrupt):
    printLog()
    raise
