#!/usr/bin/python3
"""
    matrix_devided
"""


def matrix_divided(matrix, div):
    """ matrix devided function """

    matErr = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(matErr)
    length = -1
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError(matErr)
        if (length == -1):
            length = len(item)
        if len(item) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for i in item:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(matErr)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
