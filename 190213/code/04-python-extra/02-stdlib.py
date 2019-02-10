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
