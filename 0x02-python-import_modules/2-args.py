#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argv = argv[1:]
    count = len(argv)
    num = 1
    if count == 0:
        ending = "s."
    elif count == 1:
        ending = ":"
    else:
        ending = "s:"
    print("{} argument".format(count) + ending)

    for i in argv:
        print("{}: ".format(num) + i)
        num = num + 1
