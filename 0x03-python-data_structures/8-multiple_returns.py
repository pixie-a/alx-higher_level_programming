#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    else:
        str = len(sentence)
        return (str, sentence[0])
