#!/usr/bin/python3
""" square module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Rectangle class """

    def __init__(self, size):
        Square.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {0}/{0}".format(self.__size)
