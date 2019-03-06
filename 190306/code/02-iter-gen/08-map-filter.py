#!/usr/bin/env python3

l = map(lambda x: x * 10, range(0, int(10)))
print(l)
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(list(l))

l = filter(lambda x: x % 2 == 0, range(0, int(1e9)))
print(l)
print(next(l))
print(next(l))
print(next(l))
print(next(l))

# list comprehension
l = [x * 10 for x in range(10)]
print(l)

# generator expression
l = (x * 10 for x in range(int(1e9)))  # just like map
print(l)
print(next(l))
print(next(l))
print(next(l))
# print(list(l))

print(sorted([x * 2 for x in range(10, 0, -1)]))

print(sorted((x * 2 for x in range(10, 0, -1))))

print(sorted(x * 2 for x in range(10, 0, -1)))
