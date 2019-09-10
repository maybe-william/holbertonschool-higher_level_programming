#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number < 0 and digit > 0:
    digit = -10 + digit
st = "Last digit of {:d} is {:d} and is ".format(number, digit)
if digit > 5:
    st_end = "greater than 5"
elif digit == 0:
    st_end = "0"
else:
    st_end = "less than 6 and not 0"
print(st + st_end)
