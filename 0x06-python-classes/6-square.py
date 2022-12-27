#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Represents a square being defined"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class
         Args:
            size - represents the size of the square defined
            position - a tuple having two integers
        Raises:
                TypeError: If size is not integer
                            If positionos not a tuple having two integers
                ValueError: If size is less than 0
        """
        if type(size) not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

        if type(position) not tuple and len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

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

    @property
    def position(self):
        """Retrives value of position"""

        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position"""

        if type(position) not tuple and len(position) != 2:
            raise TypeError('position must be a tupleof 2 positive integers')

        self.__position = position

    def my_print(self):
        """Prints the square in #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.size)
