#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    it = 0
    for this in my_list:
        num += this[0] * this[1]
        it += this[1]
    return (num / it)
