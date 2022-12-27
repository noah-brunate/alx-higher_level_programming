#!/usr/bin/python3

"""Defines a square"""

class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """initializing this square class
        Args: size - represents size of the square defined
        Raises:
            TypeError: If size is not integer
            ValueError: If size is less than 0
        """
        if type(size) not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
