#!/usr/bin/env python3
def my_decorator(func):
    calls = 0

    def wrapper():  # *args, **kwargs not covered
        nonlocal calls
        calls += 1
        print('called!', calls)
        func()
        print('finished!')
    return wrapper


@my_decorator
def foo():
    print('foo!')


foo()
print(foo.__name__)
print(foo.__doc__)
