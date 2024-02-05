#!/usr/bin/python3
"""
class
"""


def add_attribute(obj, key, value):
    """ add attribute """

    if (not hasattr(obj, "__dict__")):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
