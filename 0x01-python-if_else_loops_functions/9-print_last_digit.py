#!/usr/bin/python3
def print_last_digit(number):
    digit = number % 10
    if number < 0 and digit > 0:
        digit = 10 - digit
    print("{:d}".format(digit), end="")
    return digit
