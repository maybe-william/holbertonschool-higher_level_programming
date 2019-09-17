#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
        return
    for row in matrix:
        x = list(" " * (len(row) - 1))
        x.append("\n")
        y = zip(row, x)
        for tup in y:
            print("{:d}{:c}".format(tup[0], ord(tup[1])), end="")
