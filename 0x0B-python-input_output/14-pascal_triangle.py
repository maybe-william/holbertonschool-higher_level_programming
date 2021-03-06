#!/usr/bin/python3
""" module: pascal's triangle """


def pascal_triangle(n, pasc=[[1], [1, 1]]):
    """ Return a LoL of ints representing pascal's triangle up to row n """
    # memoized case
    if n <= 0:
        return []
    if len(pasc) > n - 1:
        return pasc[0:n]

    # recursive case
    prev = pascal_triangle(n - 1)
    curr = gen_next(prev[-1])
    pasc.append(curr)

    return pasc


def gen_next(row):
    """ Generate the next row given the previous """
    l = [1]
    for i in range(0, len(row) - 1):
        l.append(row[i] + row[i + 1])
    l.append(1)
    return l
