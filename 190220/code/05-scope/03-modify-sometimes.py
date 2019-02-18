#!/usr/bin/env python3
def foo(flag):
    def bar():
        print(y)
    if flag:
        y = 10
    return bar


foo(True)()
foo(False)()
