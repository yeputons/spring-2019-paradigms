#!/usr/bin/env python3
# Strong typing
print(0 + 0)
print("0" + "0")
print(0 + "0")
print(type(0))
print(type("0"))

# print("c" - "a")
# print('c' - 'a')
print(ord("c") - ord("a"))

print(int("20") - int("10"))

# Explicit conversions
# print("Hello, " + 123)
# https://docs.python.org/3/library/functions.html
print("Hello, " + str(123))
print("Hello, " + hex(123))
print("Hello, " + bin(123))

print(("a" == "a") + 10)  # Implicit from bool to int

# Demo of dynamic typing
do_something = input("Do something? ") == "yes"
print(do_something)
# print("Hello, " + do_something)
x = "foo" if do_something else 100  # Impossible in strong typing
print(type(x))
print(str(x) + "bar")
