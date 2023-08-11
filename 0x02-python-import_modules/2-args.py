#!/usr/bin/python3

def print_args(argv):
    count = len(argv) - 1
    if count == 0:
        print("{:d} arguments.".format(count))
    else:
        if count == 1:
            print("{:d} argument:".format(count))
        else:
            print("{:d} arguments:".format(count))
        for i in range(count):
            print("{:d}: {:s}".format(i + 1, argv[i + 1]))


if __name__ == "__main__":
    import sys
    print_args(sys.argv)
