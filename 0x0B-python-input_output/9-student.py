#!/usr/bin/python3
"""
module
"""


class Student:
    """ class """

    def __init__(self, first_name, last_name, age):
        """ __init__ """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to_json """

        return vars(self)
