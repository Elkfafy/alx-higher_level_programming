#!/usr/bin/python3
def magic_calculation(a, b, c):
    if (b < a):
        return c
    else:
        if (b > c):
            return a + b
        else:
            return c - a * b
