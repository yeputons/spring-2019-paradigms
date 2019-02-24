#!/usr/bin/env python3
from timeit import timeit
import numpy as np

arr = list(range(1000000))
print(timeit(
    stmt='sum(arr)',
    globals={'arr': arr},
    number=10
))

arr = np.array(arr)
print(timeit(
    stmt='arr.sum()',
    globals={'arr': arr},
    number=10
))
