#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    i = 1
    if len(sys.argv) == 0:
        print('0 arguments')
    else:
        print('len(sys.argv) arguments:')
        while(i <= len(sys.argv)):
            print('{:d}: {}'.format(i, sys.argv[i - 1]))
            i++
