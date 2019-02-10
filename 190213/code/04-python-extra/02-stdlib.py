#!/usr/bin/env python3
import collections

# https://docs.python.org/3/library/
print(sum([1, 2, 3]))
print(min([1, 2, 3]))

# https://docs.python.org/3/library/collections.html#collections.Counter
c = collections.Counter()
c.update([i % 7 for i in range(100)])
print(c)
print(c[0])

# Multiplication
print("Hi" * 2)
print([1, 2] * 3)

# Careful with references!
a = [[0, 0]] * 4
print(a)
a[0][0] = 1
print(a)
