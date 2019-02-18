#!/usr/bin/env python3
import functools


@functools.lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(100))
print(fib.cache_info())
