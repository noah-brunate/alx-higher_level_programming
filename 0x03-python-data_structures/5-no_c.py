#!/usr/bin/python3

def no_c(my_string):
    str = [n for n in my_string if n != 'c' and n != 'C']
    n_str = "".join(str)
    return n_str
