#!/usr/bin/python3
"""
myint module
"""


class MyInt(int):
    """ MyInt class """

    def __eq__(self, other):
        """ equal """

        return int(self) != other

    def __ne__(self, other):
        """ not equal """

        return int(self) == other
