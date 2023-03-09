#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    sum = 0
    count = sys.argv - 1
    for i in range(count):
        sum += int(sys.argv[i])
    print("{}".format(total))
