#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    gd = set_1.difference(set_2)
    fd = set_2.difference(set_1)
    mn = gd.union(fd)
    return mn
