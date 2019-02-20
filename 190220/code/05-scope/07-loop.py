#!/usr/bin/python
funcs = [lambda x: i + x for i in range(3)]
for f in funcs:
    print(f(10))

funcs = []
for i in range(3):
    def f(x):
        return i + x
    funcs.append(f)
for f in funcs:
    print(f(10))

funcs = []
i = 0
def f1(x):
    return i + x
funcs.append(f1)
i = 1
def f2(x):
    return i + x
funcs.append(f2)
i = 2
def f3(x):
    return i + x
funcs.append(f3)
for f in funcs:
    print(f(10))
print(f1(10))
print(f2(10))
