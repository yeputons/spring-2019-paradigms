#!/usr/bin/env python3
funcs = [lambda x: i + x for i in range(3)]
for f in funcs:
    print(f(10))


funcs = []
for i in range(3):
    def f(x):
        return i + x
    funcs.append(f)
for f in funcs:
    print(f(10))


def foo():
    funcs = []
    for i in range(3):
        def f(x):
            return i + x
        funcs.append(f)
    for f in funcs:
        print(f(10))


foo()
