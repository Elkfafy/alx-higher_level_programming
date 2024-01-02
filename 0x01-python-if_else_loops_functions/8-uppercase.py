#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            print("{:c}".format(ord(ch) - 32), end="")
        else:
            print("{:c}".format(ord(ch)), end="")
    print()
