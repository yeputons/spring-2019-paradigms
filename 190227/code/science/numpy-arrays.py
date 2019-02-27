#!/usr/bin/env python3
import numpy as np
# https://docs.scipy.org/doc/numpy/user/quickstart.html

a = np.array([[1, 2, 12],
              [3, 4, 11],
              [5, 6, 10],
              [7, 8, 9]])
print(a)
print(a.dtype)

b = np.arange(12).reshape(4, 3)
print(b)
print(np.exp(b))
print(b.transpose())

print(a + b)
print(a * b)
print(a + 10)

a[1:3, 1:2] += 100
print(a)
print(a.mean())

print(a % 2 == 0)
print(a[a % 2 == 0])

