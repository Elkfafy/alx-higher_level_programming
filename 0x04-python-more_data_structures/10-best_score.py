#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mx_key = None
    for key in a_dictionary.keys():
        if mx_key is None:
            mx_key = key
        if a_dictionary[mx_key] < a_dictionary[key]:
            mx_key = key
    return mx_key
