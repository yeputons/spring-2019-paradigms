#!/usr/bin/env python3
# http://scipy-lectures.org/advanced/sympy.html
from sympy import *

x = Symbol('x')
y = Symbol('y')

p = (x + y) ** 2
print(p)
print(diff(p, x))
print(integrate(p, x))

p = p.expand()
print(p)

p = factor(p)
print(p)

print(solve(
   [
       x + 2 * y - 3,
       2 * x + y - 6
   ],
   x, y
))

print(solve(
   [
       x ** 2 + y ** 2 - 1,
       x + y - 1
   ],
   x, y
))
