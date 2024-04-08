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

        return self._width

    @property
    def height(self):
        """ height property """

        return self._height

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val
