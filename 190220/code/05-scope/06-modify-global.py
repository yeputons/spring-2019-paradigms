#!/usr/bin/env python3
a = 10


def foo():
    # nonlocal a
    global a
    a += 1
    print(a)


foo()
foo()
foo()
