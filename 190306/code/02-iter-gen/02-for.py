#!/usr/bin/env python3

def foreach(c, f):
    it = iter(c)
    while True:
        try:
            val = next(it)
        except StopIteration:
            break
        f(val)

foreach([1, 2, 3], print)

def foreach_bad(c, f):
    it = iter(c)
    while True:
        try:
            f(next(it))
        except StopIteration:
            break

def f_strange(x):
    print('f_strange', x)
    if x == 2:
       raise StopIteration

foreach_bad([1, 2, 3], f_strange)
