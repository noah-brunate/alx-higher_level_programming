#!/usr/bin/python3
""" module defines class rectagle """


from models.base import Base


class Rectangle(Base):
    """ class rectangle inheriting from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
       """Return area of the triangle instance"""

       return (self.width * self.height)

    def display(self):
       """Prints the rectagle to stdout"""

       for y in range(self.y):
            print(" ")
       for row in range(self.height):
            for x in range(self.x):
                 print(" ", end='')
            for col in range(self.width):
                 print('#', end='')
            print()

    def __str__(self):
       """Returns details of the rectagle instance"""

       return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
       """Updates rectangle instances"""

       ln = len(args)
       if ln != 0:
            self.id = args[0]
            if ln == 2:
                 self.width = args[1]
            elif ln == 3:
                 self.width = args[1]
                 self.height = args[2]
            elif ln == 4:
                 self.width = args[1]
                 self.height = args[2]
                 self.x = args[3]
            elif ln == 5:
                 self.width = args[1]
                 self.height = args[2]
                 self.x = args[3]
                 self.y = args[4]
       elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                 if k == idl
                 elif k == "width":
                     self.width = v
                 elif k == "height":
                     self.height = v
                 elif k == "x":
                     self.x = v
                 elif k == "y":
                     self.y = v
