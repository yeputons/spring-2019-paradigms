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


def test_gcd_simple():
    assert gcd_binary(6, 8) == 2


def test_gcd_zero():
    assert gcd_binary(0, 1) == 1
    assert gcd_binary(0, 100) == 100


def test_gcd_divides():
    assert gcd_binary(4, 8) == 4
    assert gcd_binary(8, 4) == 4
    assert gcd_binary(7, 21) == 7
    assert gcd_binary(21, 7) == 7


def test_gcd_odd():
    assert gcd_binary(3 * 5 * 7, 3 * 5 * 11) == 3 * 5
    assert gcd_binary(3 * 5 * 11, 3 * 5 * 7) == 3 * 5


if __name__ == "__main__":
    import pytest
    pytest.main()
