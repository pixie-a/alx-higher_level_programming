#!/usr/bin/python3
def multiple_returns(sentence):
    str = len(sentence)
    first_char = sentence[0] if str > 0 else "None"
    return (str, first_char)
