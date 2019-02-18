#!/usr/bin/env python3
def foo(bar):
    try:
        bar()
        print('ok')
    except KeyError as err:
        print('not found', err)
    finally:
        print('finally')


a = {}
foo(lambda: print(a[10]))
a[10] = 0
foo(lambda: print(a[10]))
try:
    def bar(x):
        if not x:
            print('raising...')
            raise ValueError('x should be truthy')
        print('returning...')
    foo(lambda: bar('x'))
    foo(lambda: bar(''))
except ValueError as e:
    print('caught ValueError', e)
