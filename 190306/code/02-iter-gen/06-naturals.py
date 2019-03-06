#!/usr/bin/env python3
class Naturals:
    def __init__(self):
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.value += 1
        return self.value


it = Naturals()
for i in it:
    print(i)
