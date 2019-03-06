#!/usr/bin/env python


def foo():
    print('called!')


print(type(foo))

print(type(3))
print(dir(3))
print((3).bit_length())
print((3).numerator, (3).denominator)

print(dir(1.0))
print(1.25.as_integer_ratio())
print(1.125.as_integer_ratio())
print(1.0.is_integer())

foo()
foo.__call__()
print(type(foo.__call__))
print(dir(foo.__call__))
foo.__call__.__call__()

print(type(type(foo)))

print(foo.__name__)
foo = foo.__call__
print(foo.__name__)


def bar():
    return bar()
    return bar.__call__()
