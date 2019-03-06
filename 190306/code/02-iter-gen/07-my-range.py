#!/usr/bin/env python
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __getitem__(self, index):
        if isinstance(index, slice):
            print(index)
        else:
            if index >= self.end - self.start:
                raise KeyError(index)  # Лучше IndexError
            return self.start + index


r = MyRange(1, 10)
print(r[0])
print(r[5])
# print(r[10])
print(r[1:5])
