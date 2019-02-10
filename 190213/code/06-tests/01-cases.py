#!/usr/bin/env python3
def gcd_binary(a, b):
    """
    >>> gcd_binary(4, 8)
    4
    >>> gcd_binary(3, 7)
    1
    >>> gcd_binary(12, 8)
    4
    """
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
    # result *= max(a, b)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
