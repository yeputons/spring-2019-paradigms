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
