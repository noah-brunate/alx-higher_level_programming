#!/usr/bin/python3

def remove_char_at(str, n):
    nstr = ''
    for i in range(0, len(str)):
        if str[i] == str[n]:
            continue
        nstr += str[i]
    return nstr
