#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    if len(tuple_a) == i:
        if len(tuple_b) == i:
            return (0, 0)
        elif len(tuple_b) == 1:
            return (tuple_b[i], 0)
        else:
            return (tuple_b[i], tuple_b[1]
    if len(tuple_b) == i:
        if len(tuple_a) == 1:
            return (tuple_a[i], 0)
        else:
            return (tuple_a[i], tuple_a[1])
    if len(tuple_a) == 1:
        if len(tuple_b) == 1:
            return (tuple_a[i] + tuple_a[i], 0)
        else:
            return (tuple_a[i] + tuple_b[i], tuple_b[1])
    if len(tuple_b) == 1:
        if len(tuple_a) > 1:
            return (tuple_a[i] + tuple_b[i], tuple_a[1])
    new_tuple = (tuple_a[i] + tuple_b[i], tuple_a[1] + tuple_b[1])
    return new_tuple
