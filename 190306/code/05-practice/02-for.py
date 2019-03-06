#!/usr/bin/env python3

# Пример параметрического полиморфизма: print_all может даже
# не знать про тот класс, который ему дают, но всё равно использует.


def print_all(c):
    for x in c:
        print(x)


print_all([1, 2, 3])
print_all(range(1, 4))
