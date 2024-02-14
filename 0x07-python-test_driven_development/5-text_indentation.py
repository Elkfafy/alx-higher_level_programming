#!/usr/bin/python3
"""
module
"""


def text_indentation(text):
    """ text indentation function """

    start = True
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    for ch in text:
        if ch in ['.', '?', ':']:
            print(ch + '\n')
            start = True
        else:
            if (start == False or ch not in [' ', '\t']):
                print(ch, end='')
                continue
            start = False
