#!/usr/bin/python3
"""
class
"""


def add_attribute(obj, key, value):
    """ add attribute """

    try:
        setattr(obj, key, value)
    except Exception:
        raise TypeError("can't add new attribute")
