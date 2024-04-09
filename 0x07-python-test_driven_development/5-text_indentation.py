#!/usr/bin/python3
""" text identation module """


def text_indentation(text):
    """ text identation function """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    is_space = True
    for ch in text:
        if ch in [" ", '\t', '\n']:
            if not is_space:
                print(ch, end='')
                is_space = True
        elif ch in ['.', '?', ':']:
            print(ch + '\n')
            is_space = True
        else:
            print(ch, end='')
            is_space = False
