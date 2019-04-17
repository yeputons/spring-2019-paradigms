#!/usr/bin/env python3
def avg(l):
    l = list(l)
    return sum(l) / len(l)
print(avg(map(len, "hello good world".split())))
