#!/usr/bin/env python3
import collections.abc


class Naturals(collections.abc.Iterator):  # Подсказка для PyCharm
    def __init__(self):
        self.value = 0

    def __next__(self):
        self.value += 1
        return self.value


it = Naturals()
print(iter(it))  # Автоматически получили от Iterator
print(next(it))
print(next(it))
print(next(it))


# def is_iter(o):  # Проверка до abc
#     return hasattr(o, '__next__') and на_самом_деле_соблюдает_контракт(o):


def is_iter(o):
    return isinstance(o, collections.abc.Iterator)
