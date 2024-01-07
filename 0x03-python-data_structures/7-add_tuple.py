#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1 = 0
    num2 = 0
    for i in tuple_a[:1]:
        num1 += i
    for i in tuple_b[:1]:
        num1 += i
    for i in tuple_a[1:2]:
        num2 += i
    for i in tuple_b[1:2]:
        num2 += i
    return (num1, num2)
