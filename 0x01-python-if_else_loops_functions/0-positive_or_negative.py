#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"{number} ", end="")
if number == 0:
    print("is zero")
elif number > 0:
    print("is positive")
else:
    print("is negative")
