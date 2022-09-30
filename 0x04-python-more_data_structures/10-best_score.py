#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    for i, j in a_dictionary.items():
        if j == max(a_dictionary):
            return i
