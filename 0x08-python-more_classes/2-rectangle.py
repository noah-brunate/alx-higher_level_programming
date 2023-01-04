#!/usr/bin/python3

"""Module defines a rectagle"""


class Rectagle:
    """Class represent a rectagle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """property getter for the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """property setter for the height"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Method calculates area of rectagle
        Return: area of the triagle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Method calculates perimeter of rectagle
        Return: calculated perimeter"""

        if (self.__width or self.__height) == 0:
            return 0
        else:
            return 2 * (self.__width * self.__height)
