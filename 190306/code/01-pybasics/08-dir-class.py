#!/usr/bin/env python3
class Foo:
    def __init__(self, value):
        self.value = value

    def foo(self):
        print('foo')


foo = Foo(10)
print(dir(foo))
print(foo.__dict__)
