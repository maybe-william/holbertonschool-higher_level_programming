#!/usr/bin/python3
def remove_char_at(str, n):
    ret = ""
    for i in range(len(str)):
        if i != n:
            ret = ret + str[i]
    return ret
