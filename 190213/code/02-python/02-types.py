#!/usr/bin/env python3
print(0 + 0)
print("0" + "0")
# print(0 + "0")
print(type(0))
print(type("0"))

# print("c" - "a")
# print('c' - 'a')
print(ord("c") - ord("a"))

print(int("20") - int("10"))

# print("Hello, " + 123)
# https://docs.python.org/3/library/functions.html
print("Hello, " + str(123))
print("Hello, " + hex(123))
print("Hello, " + bin(123))

do_something = input("Do something? ") == "yes"
print(do_something)
# print("Hello, " + do_something)
print(10 + do_something)  # Implicit from bool to int
x = "foo" if do_something else 100
print(type(x))
print(str(x) + "bar")
