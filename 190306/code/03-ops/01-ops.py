#!/usr/bin/env python3

"""
Аргументы против перегрузки:
(a + b) * c  # Как бы быстро
a.add(b).multiply(c)  # Понятно же, что медленно

a || b  # Параллельность прямых ^_^
ТАК НЕ НАДО!
1. || всё ещё остаётся исходный приоритет: a || b > 0
2. || - логическое "или", "параллельность" - неочевидно

vec a, b;
a * b;  # Какое именно произведение - векторное или скалярное?
"""


class MyInt:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, MyInt):
            return MyInt(self.value + other.value)
        if isinstance(other, int):
            return MyInt(self.value + other)
        return NotImplemented  # Чтобы попробовали __radd__ или TypeError

    def __radd__(self, other):  # reverse add
        return self + other


a = MyInt(3)
b = MyInt(5)
assert str(a) == '3'
print(a)
print(b)
print(a + b)
print(a + 3)
print(3 + a)


class MyOtherInt:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'o' + str(self.value)

    def __add__(self, other):
        if isinstance(other, (MyInt, MyOtherInt)):
            return MyOtherInt(self.value + other.value)
        if isinstance(other, int):
            return MyOtherInt(self.value + other)

    def __radd__(self, other):
        return self + other


c = MyOtherInt(10)
print(c + a)
print(a + c)

print(c.__add__(a))
print(a.__radd__(c))
