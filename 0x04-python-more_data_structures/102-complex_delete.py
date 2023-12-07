#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    for ke in keys:
        if a_dictionary[ke] == value:
            del a_dictionary[ke]
    return a_dictionary
