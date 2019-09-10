#!/usr/bin/python3
def uppercase(str):
    low = str + "\n"
    for i in low:
        if ord(i) > 96 and ord(i) < 123:
            print("{:c}".format(ord(i) - 32), end="")
        else:
            print("{:c}".format(ord(i)), end="")
