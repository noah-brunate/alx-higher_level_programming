#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = 'None'
        return sentence[0]
    str_tuple = ('sentence[0]', 'len(sentence)')
    return str_tuple
