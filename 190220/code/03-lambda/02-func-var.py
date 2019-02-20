#!/usr/bin/env python3
def foo_1(x):
    """Adds ten to x"""
    return x + 10
print(foo_1(2))
print(foo_1.__name__)
print(foo_1.__doc__)

foo_2 = foo_1
print(foo_2(2))
print(foo_2.__name__)
print(foo_2.__doc__)

foo_3 = lambda x: x + 10
print(foo_3(2))
print(foo_3.__name__)
print(foo_3.__doc__)
print(list(map(lambda x: x + 10, [1, 2, 3])))

print(globals()['foo_3'](100))
