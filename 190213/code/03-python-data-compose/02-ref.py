#!/usr/bin/env python3
# https://www.oreilly.com/library/view/python-in-a/0596001886/ch04s03.html
a = [1, 2, 3]
b = [4, 5, 6]
ab = (a, b)
print(ab)

ab[0].append(10)  # ab[0] is a reference
print(ab)

cd = ab
print(ab, cd)

ab[0].append(10)
print(ab, cd)  # cd is a reference too

# Immutable objects (e.g. str) behave like "values"
s = "foo"
s = s + "bar"
s += "bar"  # shorthand
ss = (s, s)
# s[0] += "baz"

# == vs is
print([1, 2] == [1, 2])
print([1, 2] is [1, 2])
a = 10000 * 10000
b = 100000000
print(a == b)
print(a is b)
print(a is a)
print(b is b)
print(1 is 1)

# Special type/value: None, like NULL
print(None is None)
print(None == None)
print([1, 2] == None)
print([1, 2] is None)
# Idiom: is, not ==
