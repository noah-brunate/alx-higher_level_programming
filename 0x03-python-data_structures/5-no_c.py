#!/usr/bin/python3

def no_c(my_string):
    for i in my_string:
        if i == 'c':
            new_string = my_string.translate({ord('c'): None})
            break
    for i in new_string:
        if i == 'C':
            nw_string = new_string.translate({ord('C'): None})
            return nw_string
        print()
