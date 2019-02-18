#!/usr/bin/env python3
def make_func(i):
    return lambda x: i + x

funcs = map(make_func, range(3))
for f in funcs:
    print(f(10))
