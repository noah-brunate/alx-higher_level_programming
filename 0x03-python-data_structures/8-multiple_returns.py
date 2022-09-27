#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        str_let = None
    else:
        str_let = sentence[0]
    str_tuple = (len(sentence), str_let)
    return str_tuple
