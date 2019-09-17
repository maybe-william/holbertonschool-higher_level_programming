#!/usr/bin/python3


def multiple_returns(sentence):
    return (0, None) if len(sentence) == 0
    return (len(sentence), sentence[0])
