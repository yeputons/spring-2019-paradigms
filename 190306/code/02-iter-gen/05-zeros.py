#!/usr/bin/env python3

class Zeros:
    def __iter__(self):
        return self

    def __next__(self):
        return 0

it = Zeros()
print(next(it))
print(next(it))
print(next(it))
print(next(it))
for i in it:
    print(i)
