#!/usr/bin/python3
""" print square module """


def print_square(size):
    """ print square function """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
