#!/usr/bin/env python3
# Code/data primitives
i = 0
i += 1
print("Hello World")  # Careful	 with Cyrillic

name = input('Your name> ')  # Both quotes work, see codestyle, I like double
print("Hello, {}".format(name))

# For loop iterates over a 'list' or 'collection',
# let's start with range().
for i in range(10):
    print("1: i=", i)  # Mind the indent

for i in range(10, 0, -2):
    print("2: i={}".format(i))

# While loop
a = 0
b = 1
while b < 100:
    ab = a + b
    a = b
    b = ab
print(b)

# If statement, 'and'
if b % 2 == 0 and 2 * 2 == 4:
    print("Even")
else:
    print("Odd")
# Ternary operator
print("Even" if b % 2 == 0 else "Odd")

# Mind two different divisions! Esp. Python 3
print(b / 100)
print(b // 100)
