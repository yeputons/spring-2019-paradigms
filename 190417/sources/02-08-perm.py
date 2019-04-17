#!/usr/bin/env python3
def permute(a, p):
    for i in range(len(a)):
        a[i] = a[p[i]]

a = [10, 11, 10, 12, 9]
p = [ 2,  0,  0,  4, 4]
permute(a, p)
assert a == [10, 10, 10, 9, 9]

a = [10, 11, 13, 12, 9]
p = [ 2,  0,  0,  4, 4]
permute(a, p)
print(a)
assert a == [13, 10, 10, 9, 9]
