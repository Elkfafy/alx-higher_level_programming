#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    cond_1 = (i for i in set_1 if i not in set_2)
    cond_2 = (i for i in set_2 if i not in set_1)
    return set(list(cond_1) + list(cond_2))
