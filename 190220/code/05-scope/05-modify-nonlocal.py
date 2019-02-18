#!/usr/bin/env python3
def foo(a):
    def bar(b):
        nonlocal a
        a += 1
        return a + b
    print(bar(10))
    a = 5
    print(bar(10))
    return bar


bar_1 = foo(1)
print(bar_1(100))
bar_2 = foo(2)
print(bar_2(100))
