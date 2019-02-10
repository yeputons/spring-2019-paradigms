#!/usr/bin/env python3
# Tuples are heterogeneous
a = (1, 2, "foo", "bar")
print(a)
print(a + (3, 4))
print(a[0])
# Slices
print(a[0:2])
print(a[0:4:2])
print(a[0::2])
# a[0] = 3  # Immutable

# Unpacking
a0, a1, a2, a3 = a
print(a0, a1, a2, a3)
a1, a0 = a0, a1
print(a0, a1)
# a0, a1 = a
a0, *ax = a
print(a0, ax)

# Lists are heterogenous (rarely used)
a = [1, 2, "foo", "bar"]
print(a)
print(a + [3, 4])
print(a[0])
a[0] = 3  # Mutable
print(a)

# Lists can be unpacked
x, y = [10, 20]
print(x, y)
# x, y = [10, 20, 30]

# And modified
a.append(100)
print(a)

# List comprehension
print([x + 2 for x in range(10)])
print([x + 2 for x in range(10) if x < 5])

# Note that range is not a list:
x = range(1, 10000000000)
print(x)
print(x[1:10])
print(list(x[1:10]))

# Strings
print("foo")
print([x for x in "foo"])
print(list("foo"))  # https://docs.python.org/3/library/

# Strings vs bytes (Python 3)
print(ord('ы'))  # 1099??! https://www.compart.com/en/unicode/U+044B
print(hex(ord('ы')))  #  https://www.compart.com/en/unicode/U+044B
print('ы'.encode('utf-16'))
print(list('ы'.encode('utf-16')))
print(list('ы'.encode('utf-8')))
print(list('ы'.encode('1251')))
