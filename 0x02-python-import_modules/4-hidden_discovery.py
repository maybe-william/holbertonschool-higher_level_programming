#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    def good(x):
        y = len(x) < 2 or (x[0] != '_' and x[1] != '_')
        return y

    q = sorted(filter(good, dir(hidden_4)))
    for i in q:
        print(i)
