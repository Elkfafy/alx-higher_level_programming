#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    try:
        for alist in matrix:
            for item in alist[:-1]:
                print("{:d}".format(item), end=" ")
            for item in alist[-1:]:
                print("{:d}".format(item), end="")
            print()
    except TypeError:
        return
