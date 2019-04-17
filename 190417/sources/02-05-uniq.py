#!/usr/bin/env python3
def foo(xs):
    res = []
    if not xs:
        return
    res.append(xs[0])
    for x in xs[1:]:
        if res[-1] != x:
            res.append(x)
    return res

assert foo([10, 10, 20, 10]) == [10, 20, 10]
assert foo([10, 10, 20, 20, 10, 10]) == [10, 20, 10]
