#!/usr/bin/python3
"""
mylist module
"""


class MyList(list):
    """ mylist class """

    def print_sorted(self):
        """ print_sorted """

        temp = [i for i in self]
        temp.sort()
        print(temp)
