#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @width.setter
    def width(self, value):
        self.__width = value
    @height.setter
    def height(self, value):
        self.__height = value
