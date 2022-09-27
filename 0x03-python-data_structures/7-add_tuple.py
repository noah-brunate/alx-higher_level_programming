#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    while i < 2:
        if len(tuple_a) == i:
            tuple_a[i] = 0
            return tuple_a
        if len(tuple_b) == i:
            tuple_b[i] = 0
            return tuple_b
        if i == 0:
            sum_1 = sum(tuple_a[i], tuple_b[i])
            return sum_1
        if i == 1:
            sum_2 = sum(tuple_a[i], tuple_b[i])
            return sum_2
        i += 1
    new_tuple = ('sum_1', 'sum_2')
    return new_tuple
