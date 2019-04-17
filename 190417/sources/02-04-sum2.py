#!/usr/bin/env python3
def sum(xs):
    a = 0
    for x in xs:
        a += x
    return a

assert sum([1, 2, 3]) == 6
