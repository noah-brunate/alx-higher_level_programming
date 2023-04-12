#!/usr/bin/python3
""" Module write a string to a file """


def write_file(filename="", text=""):
    """
        function writes a string to a file
        Args:
            filename: file to write to
            text: string to write
        Returns:
            returns the number of characters written to the file
    """

    num = 0
    with open('filename', 'w') as f:
        for ch in text:
            f.write(ch)
            num += 1
    return num
