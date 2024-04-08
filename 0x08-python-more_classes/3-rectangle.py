#!/usr/bin/python3
""" rectangle module """


class Rectangle:
    """ rectangle """

    def __init__(self, width=0, height=0):
        """
            initialize the rectangle
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """ width property """

        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """ height property """

        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        data = ['#' * self.wdith for _ in range(self.height)].join()
        return data
