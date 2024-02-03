#!/usr/bin/python3
"""
square module
"""


class Square:
    """
    square class
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        error_message = "position must be a tuple of 2 positive integers"
        if (not isinstance(value, tuple)):
            raise TypeError(error_message)
        elif (len(value) != 2):
            raise TypeError(error_message)
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError(error_message)
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.size == 0):
            print()
            return
        for i in range(0, self.position[1]):
            print()
        for i in range(0, self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
