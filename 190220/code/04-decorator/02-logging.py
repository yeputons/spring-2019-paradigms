#!/usr/bin/env python3
def my_decorator(func):
    calls = 0

    def wrapper():  # Can also add *args, **kwargs
        nonlocal calls  # MAGIC, TBD later
        calls += 1
        print('called!', calls)
        func()
        print('finished!')
    return wrapper


@my_decorator  # foo = my_decorator(foo)
def foo():
    print('foo!')


foo()
print(foo.__name__)
print(foo.__doc__)
