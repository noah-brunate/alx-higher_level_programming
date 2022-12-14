#!/usr/bin/python3

"""Module defines a rectagle"""


class Rectagle:
    """Class represent a rectagle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
	Args:
		width - represents the width of the rectagle
		height - represent the height of the rectagle
	Raises:
		TypeError - if size is not integer
		ValueError - if size is less than zero
	"""
        self.__width = value
	self.__height = value

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
