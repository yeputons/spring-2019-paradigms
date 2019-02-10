#!/usr/bin/env python3
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing
print("Yes" if 2 == 2 else "No")
print("Yes" if 0 else "No")
print("Yes" if 1 else "No")
print("Yes" if 0.5 else "No")
print("Yes" if 0.0 else "No")
print("Yes" if "no" else "No")
print("Yes" if "" else "No")
print("Yes" if [1, 2, 3] else "No")
print("Yes" if [] else "No")
print("Yes" if [0] else "No")
print("Yes" if {} else "No")

x = [1, 2, 3]
if len(x) > 0:  # Bad
    print(x[0])
if x:  # Good
    print(x[0])
