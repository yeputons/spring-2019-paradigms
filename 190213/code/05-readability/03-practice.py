#!/usr/bin/env python3
def valid_palindrome(s):
    """
    >>> valid_palindrome("aba")
    True
    >>> valid_palindrome("abba")
    True
    >>> valid_palindrome("foofoo")
    False
    >>> valid_palindrome("")
    True
    >>> valid_palindrome("abcdba")
    False
    """
    return False


def reverse_bits(n):
    """
    >>> reverse_bits(6)
    3
    >>> reverse_bits(100)
    19
    """
    return n


# https://leetcode.com/problems/walking-robot-simulation/
def walking_robot_simulation(commands, obstacles):
    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
