#!/usr/bin/python3
""" This module divides a matrix """


def matrix_divided(matrix, div):
    """ Divide a l o l of floats by a number """
    materr = "matrix must be a matrix (list of lists) of integers/floats"
    rowerr = "Each row of the matrix must have the same size"
    numerr = "div must be a number"
    zeroerr = "division by zero"
    if type(matrix) is not list:
        pass
    if type(matrix[0]) is not list:
        pass
    if type(matrix[0][0]) is not int and type(matrix[0][0]) is not float:
        pass
    if type(div) is not int and type(div) is not float:
        pass
    if div == 0:
        pass
