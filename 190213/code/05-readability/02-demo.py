#!/usr/bin/env python3
# Just run this file like `python 02-demo.py` to run doctest,
# see the bottom of the file for magic lines.


def reverse_integer(x):
    """
    >>> reverse_integer(1234567890123)
    3210987654321
    >>> reverse_integer(0)
    0
    >>> reverse_integer(120)
    21
    """
    digits = []
    while x > 0:  # 6. Replace with str()
        digits.append(x % 10)
        x //= 10
    n = len(digits)  # 5. No need after following refactorings
    for i in range(n // 2):  # 2. Use list(reversed(digits))
        # 1. digits[i], digits[n - i - 1] = digits[n - i - 1], digits[i]
        tmp = digits[n - i - 1]
        digits[n - i - 1] = digits[i]
        digits[i] = tmp
    # 4. enumerate();
    # 7. Convert list to string with join().
    # 8. Convert string to int.
    for i in range(n):
        ten = 1
        for j in range(i):  # 3a. Underscore; 3b. 10 ** i
            ten *= 10
        x += ten * digits[i]
    print(x)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
