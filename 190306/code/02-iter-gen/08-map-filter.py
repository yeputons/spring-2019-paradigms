#!/usr/bin/env python3

lst = map(lambda x: x * 10, range(0, int(10)))
print(lst)
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
print(list(lst))

lst = filter(lambda x: x % 2 == 0, range(0, int(1e9)))
print(lst)
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))

# list comprehension
lst = [x * 10 for x in range(10)]
print(lst)

# generator expression
lst = (x * 10 for x in range(int(1e9)))  # Как map()
print(lst)
print(next(lst))
print(next(lst))
print(next(lst))
# print(list(lst))

print(sorted([x * 2 for x in range(10, 0, -1)]))

print(sorted((x * 2 for x in range(10, 0, -1))))

print(sorted(x * 2 for x in range(10, 0, -1)))  # Сахар
