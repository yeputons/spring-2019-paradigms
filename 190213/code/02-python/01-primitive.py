#!/usr/bin/env python3
# Code/data primitives
i = 0
i += 1
print("Hello World")  # Careful	 with Cyrillic

name = input('Your name> ')  # Both quotes work, see codestyle, I like double
print("Hello, {}".format(name))

for i in range(10):
    print("1: i=", i)  # Mind the indent

for i in range(10, 0, -2):
    print("2: i={}".format(i))

a = 0
b = 1
while b < 100:
    ab = a + b
    a = b
    b = ab
print(b)

if b % 2 == 0 and 2 * 2 == 4:
    print("Even")
else:
    print("Odd")
print("Even" if b % 2 == 0 else "Odd")

if 2 * 2 == 4: print("ok")

print(b / 100)
print(b // 100)
