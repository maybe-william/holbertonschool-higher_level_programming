#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return 0
    cumul = 0
    weight = 0
    for i in my_list:
        cumul = cumul + (i[0] * i[1])
        weight = weight + i[1]
    return cumul / weight
