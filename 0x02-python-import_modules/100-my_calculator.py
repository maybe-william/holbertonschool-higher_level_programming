#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    def p_out(op, func):
        a = argv[1]
        b = argv[3]
        print("{} {} {} = {}".format(a, op, b, func(int(a), int(b))))

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if argv[2] == '+':
        p_out('+', add)
    elif argv[2] == '-':
        p_out('-', sub)
    elif argv[2] == '*':
        p_out('*', mul)
    elif argv[2] == '/':
        p_out('/', div)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
