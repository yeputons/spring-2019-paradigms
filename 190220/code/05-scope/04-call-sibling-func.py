#!/usr/bin/env python3
def foo(flag):
    def bar():
        baz()
    if flag:
        def baz():
            print('foo.bar.baz1')
    else:
        def baz():
            print('foo.bar.baz2')
    return bar


foo(True)()
foo(False)()
