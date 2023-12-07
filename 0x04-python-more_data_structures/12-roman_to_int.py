#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [roman_number[n] for n in roman_string] + [0]
    x = 0
    for i in range(len(num) - 1):
        if num[i] >= num[i+1]:
            x += num[i]
        else:
            x -= num[i]
    return x
