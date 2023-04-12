#!/usr/bin/python3
""" Module reads a text file and prints it to stdout """


def read_file(filename=""):
    """
        function reads a text file and prints the content to stdout
        Args:
            filename: text file to be printed
    """

    with open('filename') as f:
        for line in f:
            print(line, end='')
