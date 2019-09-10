#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        th = i % 3 == 0
        fv = i % 5 == 0
        ftn = i % 15 == 0
        if ftn:
            rep = "FizzBuzz "
        elif th:
            rep = "Fizz "
        elif fv:
            rep = "Buzz "
        else:
            rep = str(i) + " "
        print(rep, end="")
