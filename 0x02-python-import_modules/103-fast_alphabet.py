#!/usr/bin/python3
from functools import reduce as r
print(r(lambda x, y: (x + y), map(chr, range(65, 91))))
