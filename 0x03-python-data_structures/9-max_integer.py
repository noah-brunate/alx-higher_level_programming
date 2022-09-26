#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ('none')
    i = 0
    while i < len(my_list):
        for j in my_list:
            if my_list[i] < j:
                break
            if j = my_list[len(my_list) - 1]:
                return my_list[i]
        i += 1
