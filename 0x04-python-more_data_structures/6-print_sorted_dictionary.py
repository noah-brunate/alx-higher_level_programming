#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    nkeys = list(a_dictionary.keys())
    nkeys.sort()
    n_dic = {i: a_dictionary[i] for i in nkeys}
    for i, j in n_dic.items():
        print('{}: {}'.format(i, j))

