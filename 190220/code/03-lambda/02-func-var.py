#!/usr/bin/env python3
foo_1 = lambda x: x + 10
def foo_2(x):
    """Adds something"""
    return x + 10
foo_3 = foo_2

l = [1, 2, 3]
print(list(map(foo_1, l)))
print(list(map(foo_2, l)))
print(list(map(foo_3, l)))

print(foo_2.__name__, foo_2.__doc__)
print(foo_3.__name__, foo_3.__doc__)
print(foo_1.__name__, foo_1.__doc__)
