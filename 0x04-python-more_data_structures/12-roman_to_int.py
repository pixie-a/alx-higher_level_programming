#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [roman[n] for n in roman_string] + [0]
    x = 0
    for i in range(len(num) - 1):
        if num[i] >= num[i+1]:
            x += num[i]
        else:
            x -= num[i]
    return x
