#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    gd = set_1.difference(set_2)
    return gd

set_1 = { "Python", "C", "Javascript" }

set_2 = { "Bash", "C", "Ruby", "Perl" }
print(only_diff_elements(set_1, set_2))
