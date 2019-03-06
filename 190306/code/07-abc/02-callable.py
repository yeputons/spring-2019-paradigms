#!/usr/bin/env python3
import collections.abc


class MyFunc(collections.abc.Callable):
    def __call__(self):
        return 0


f = MyFunc()
print(f())
