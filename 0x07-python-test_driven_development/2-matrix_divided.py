#!/usr/bin/python3
"""
    module
"""


def is_integer_or_float(num, err_msg):
    """ is integer or float function """

    if (not isinstance(num, int) and not isinstance(num, float)):
        raise TypeError(err_msg)


def is_matrix(matrix):
    """ matrix is a list """

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(matrix_error)
    for alist in matrix:
        if not isinstance(alist, list):
            raise TypeError(matrix_error)
        for item in alist:
            is_integer_or_float(item, matrix_error)
    if len(matrix) == 0:
        raise TypeError(matrix_error)
    size = len(matrix[0])
    for alist in matrix:
        if size != len(alist):
            raise TypeError("Each row of the matrix must have the same size")


def matrix_divided(matrix, div):
    """ matrix divided function """

    is_integer_or_float(div, "div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    is_matrix(matrix)
    return [[round(item / div, 2) for item in alist] for alist in matrix]
