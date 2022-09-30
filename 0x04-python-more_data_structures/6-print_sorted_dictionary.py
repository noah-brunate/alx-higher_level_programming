#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortd = sorted(a_dictionary)
    for i ,j in a_dictionary:
        if i == '':
            print('{}: {}'.format(i, j))
