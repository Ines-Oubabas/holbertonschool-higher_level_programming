#!/usr/bin/python3
"""define print square"""


def print_square(size):
    """print square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
