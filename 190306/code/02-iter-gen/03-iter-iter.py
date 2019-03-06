#!/usr/bin/env python3

x = [1, 2, 3]
for i in x:
    print(i)

it = iter(x)  # Чтобы можно было делать for по итератору.
assert iter(it) is it

print(next(it))
for i in it:
    print('for:', i)
