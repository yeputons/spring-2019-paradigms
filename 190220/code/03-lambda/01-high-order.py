#!/usr/bin/env python3
l = [1, 2, 3]
print([x for x in l if x != 2])

def x_is_not_2(x):
    return x != 2
print(list(filter(x_is_not_2, l)))

l = ['1', '2', '3']
print(sum(map(int, l)))
print(sum([int(x) for x in l]))
