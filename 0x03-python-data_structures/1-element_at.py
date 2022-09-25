#!/usr/bin/python3

def element_at(my_list, idx):
    for i in my_list:
        if i == idx:
            if idx < 0 and idx > len(my_list):
                return none
            else:
                return idx
            print()
