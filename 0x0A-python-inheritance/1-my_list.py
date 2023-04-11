#!/usr/bin/python3
""" Module has a class Mylist that inheritees from list """


class Mylist(list):
    """ class in heritaes from list and has a public instance method print_sorted """

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self)) 
