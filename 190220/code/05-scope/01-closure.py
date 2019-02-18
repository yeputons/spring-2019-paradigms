#!/usr/bin/env python3
def make_plus(a):
    def func(b):
        return a + b
    return func


plus_2 = make_plus(2)
plus_3 = make_plus(3)
print(plus_2(10), plus_3(10))
