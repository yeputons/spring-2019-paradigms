#!/usr/bin/env python3
import itertools


def naturals():  # Не функция, а генератор, потому что есть 'yield'
    i = 1
    while True:
        yield i
        i += 1


it = naturals()
print(it)
print(next(it))
print(next(it))
print(next(it))


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


it = fib()
print(it)
print(list(itertools.islice(it, 5, 10)))
print(next(it))
print(next(it))


def foo():
    yield 1
    yield 2
    yield 3


print(list(foo()))
