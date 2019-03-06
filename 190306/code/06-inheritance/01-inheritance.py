#!/usr/bin/env python3
class MyBaseClass:
    def __init__(self):
        print('inited MyBaseClass')

    def foo(self):
        print('foo')


class MyDerivedClass(MyBaseClass):
    def __init__(self):
        super().__init__()
        print('inited MyDerivedClass')

    def foo(self):
        print('foo2')
        super().foo()


x = MyDerivedClass()
x.foo()

print(isinstance(x, MyDerivedClass))
print(isinstance(x, MyBaseClass))
print(type(x) == MyDerivedClass)
print(type(x) == MyBaseClass)
