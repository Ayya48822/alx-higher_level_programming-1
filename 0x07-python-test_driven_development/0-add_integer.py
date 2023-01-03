#!/usr/bin/python3
""" the add function"""


def add_integer(a, b=98):
    """ adds integers

    Args:
        @a: the first argument
        @b: the second argument default to 98 if not given
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
