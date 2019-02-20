#!/usr/bin/env python3
import functools


def my_decorator(func):
    calls = 0

    @functools.wraps(func)  # Read about idioms!
    def wrapper():
        nonlocal calls  # MAGIC, TBD later
        calls += 1
        print('called! {}'.format(calls))
        func()
        print('finished!')
    # wrapper.__name__ = func.__name__  # replaced by .wraps()
    return wrapper


@my_decorator
def foo():
    print('foo!')


foo()
foo()
foo()
print(foo.__name__)
print(foo.__doc__)
