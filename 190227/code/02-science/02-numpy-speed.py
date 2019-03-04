#!/usr/bin/env python3
from timeit import timeit
import numpy as np

arr = list(range(10000)) * 100
print(timeit(
    stmt='sum(arr)',
    globals={'arr': arr},
    number=10
))

np_arr = np.array(arr)
print(timeit(
    stmt='np_arr.sum()',
    globals={'np_arr': np_arr},
    number=10
))
