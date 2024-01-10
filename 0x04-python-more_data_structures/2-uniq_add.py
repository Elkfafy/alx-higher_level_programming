#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_dict = {}
    sum = 0
    for i in my_list:
        if i not in my_dict:
            sum += i
        my_dict[i] = "found"
    return sum
