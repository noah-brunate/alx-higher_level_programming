#!/usr/bin/python3
""" Module appends a string to a file """


def append_file(filename="", text=""):
    """
        function appends a string to a file
        Args:
            filename: file to append the string
            text: string to append
        Returns:
            returns the number of characters appended to the file
    """

    num = 0
    with open('filename', 'a') as f:
        for ch in text:
            f.write(ch)
            num += 1
    return num
