#!/usr/bin/env python3
from math import gcd


def gcd_binary(a, b):
    result = 1
    while a and b:
        if a % 2 == b % 2 == 0:
            result *= 2
            a //= 2
            b //= 2
        elif a % 2 == 0:
            a //= 2
        elif b % 2 == 0:
            b //= 2
        elif a >= b:
            a -= b
        else:
            b -= a
    result *= max(a, b)
    return result


def test_gcd():
    assert gcd_binary(4, 8) == 4


def test_gcd_all():
    for i in range(1, 100):
        for j in range(1, 100):
            assert gcd_binary(i, j) == gcd(i, j)


if __name__ == "__main__":
    import pytest
    pytest.main()
