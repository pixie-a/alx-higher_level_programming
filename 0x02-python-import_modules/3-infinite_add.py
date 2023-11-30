#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    def arg(argv):

        arg(sys.argv)
        x = len(argv) - 1
        if x == 0:
            print("{}".format(x))
        else:
            result = 0
            i = 1
            while i <= x:
                result += int(argv[i])
                i += 1
            print("{}".format(result))
