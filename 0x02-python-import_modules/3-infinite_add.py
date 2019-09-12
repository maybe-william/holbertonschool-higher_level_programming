#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argv = argv[1:]
    argv = map(int, argv)
    print(str(sum(argv)))
