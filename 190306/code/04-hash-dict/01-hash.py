#!/usr/bin/env python3

class MyInt:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

a1 = MyInt(3)
a2 = MyInt(3)
b = MyInt(5)
print(hash(1e100))
print(hash(a1))
print(hash(a2))
d = {
  a1: 'val1a',
  a2: 'val1b',
  b: 'val2'
}
print(d)

def check_contract(a, b):
    if a == b:
        assert hash(a) == hash(b)
    # Java: o.hashCode(), o.equals(b)

"""
# Нельзя класть изменяемые объекты в словари!
l = [1, 2, 3]
d[l] = 'key'
l.append(4)
print(d[l]) # Упс
"""

def str_hash(s):
    result = 0
    for c in s:
        # Взять по модулю!
        result = (result * 239017 + ord(c))
    return result % (2 ** 32)
print(str_hash('xxxxxxxxxxxx'))
print(str_hash('x' * 100000))
