#!/usr/bin/env python3
from functools import total_ordering


@total_ordering  # Чтобы не писать руками и __le__
class MyInt:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    # less than
    def __lt__(self, other):
        return self.value < other.value


a = MyInt(3)
b = MyInt(5)
print(a == b)
print(a == MyInt(3))
print(a < MyInt(3), a < MyInt(4))
print(a > MyInt(3), a > MyInt(4))  # __gt__ выводится из __lt__
print(a <= MyInt(3), a >= MyInt(4))
