#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argL = len(sys.argv) - 1
    if argL == 0:
        print("{} arguments.".format(argL))
    elif argL == 1:
        print("{} argument:".format(argL))
    else:
        print("{} arguments:".format(argL))
    for i in range(argL):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
