#!/usr/bin/python3
"""
module
"""


def text_indentation(text):
    """ text indentation function """

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    for ch in text:
        if ch in ['.', '?', ':']:
            print(ch + '\n')
        else:
            print(ch, end='')
