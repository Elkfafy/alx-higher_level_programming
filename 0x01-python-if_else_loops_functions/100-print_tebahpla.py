#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{:c}".format(i + 97 * (i % 2) + 65 * (not (i % 2))), end="")
