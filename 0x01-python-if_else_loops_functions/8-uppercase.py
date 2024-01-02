#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            out = ord(ch) - 32
        else:
            out = ord(ch)
        print("{:c}".format(out), end="")
    print()
