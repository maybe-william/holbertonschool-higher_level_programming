#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divide each list1 by list2 elem by elem and return new list"""
    ret = []
    for i in range(0, list_length):
        item = 0
        try:
            item = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            ret.append(item)
    return ret
