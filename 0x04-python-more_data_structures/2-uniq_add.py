#!/usr/bin/python3

def uniq_add(my_list=[]):
    gd = set()
    for i in my_list:
        gd.append(i)
    sam = 0
    for j in gd:
        sam += j
    return sam
