#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    size = len(a_dictionary)
    n_dictionary = a_dictionary.copy()
    for i, j in a_dictionary.items():
        if j == value:
            a_dictionary.pop(i)
    if len(a_dictionary) == size:
        return n_dictionary
    else:
        return a_dictionary
