#!/usr/bin/python3
""" This module divides a matrix """


def matrix_divided(matrix, div):
    """ Divide a l o l of floats by a number """
    materr = "matrix must be a matrix (list of lists) of integers/floats"
    rowerr = "Each row of the matrix must have the same size"
    numerr = "div must be a number"
    zeroerr = "division by zero"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(materr)
    llen = None
    for r in matrix:
        if type(r) is not list:
            raise TypeError(materr)
        if llen is None:
            llen = len(r)
        if len(r) != llen:
            raise TypeError(rowerr)
        for item in r:
            if type(item) is not int and type(item) is not float:
                raise TypeError(materr)
    if type(div) is not int and type(div) is not float:
        raise TypeError(numerr)
    if div == 0:
        raise ZeroDivisionError(zeroerr)

    return [[round(j / div, 2) for j in i] for i in matrix]
