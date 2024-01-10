#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    sum = 0
    max = 'I'
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for ch in reversed(list(roman_string)):
        if roman[ch] == roman[max]:
            sum += roman[ch]
        elif roman[ch] > roman[max]:
            sum += roman[ch]
            max = ch
        else:
            sum -= roman[ch]
    return sum
