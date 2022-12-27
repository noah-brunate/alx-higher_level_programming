#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Represents a square being defined"""

    def __init__(self, size=0):
        """Initializing this square class
         Args:
            size - represents the size of the square defined
            Raises:
                TypeError: If size is not integer
                ValueError: If size is less than 0
        """
        if type(size) not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Calculates the current square area
        Return:the square of size"""

        return (self.__size ** 2)

    @property
    def size(self):
        """Retrives the size os square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""

        if type(size) not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Calculates the current square area
            Return:the square of size"""

        return (self.__size ** 2)

    def my_print(self):
        """prints the square in #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
