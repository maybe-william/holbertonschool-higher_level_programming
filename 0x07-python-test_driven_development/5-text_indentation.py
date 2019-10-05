#!/usr/bin/python3
""" This module prints a string with text indentation """


def rmchr(txt, char):
    """ Remove char from txt and add \n\n """
    tempstr = txt
    ret = ""
    tup = tempstr.partition(char)
    while tup[1] != "":
        ret = ret + tup[0].rstrip("\t\v\f ") + tup[1] + "\n\n"
        tempstr = tup[2].lstrip("\t\v\f ")
        tup = tempstr.partition(char)
    ret = ret + tempstr
    return ret


def text_indentation(text):
    """ Indent the text after ? . or : """
    if type(text) is not str:
        raise TypeError("text must be a string")

    tmp = text
    tmp = rmchr(tmp, "?")
    tmp = rmchr(tmp, ".")
    tmp = rmchr(tmp, ":")
    print(tmp, end="")
