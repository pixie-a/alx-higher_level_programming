#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        if i * 10 + j < 89:
            print("{}{}".format(i, j), end=", ")
        else:
            print("{}".format(89))
