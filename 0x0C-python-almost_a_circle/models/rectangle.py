#!/usr/bin/python3
""" module that contains form class rectangle inherits from class base"""
from models.base import Base


class Rectangle(Base):
    """ class rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ creating the init function

        Args:
            @width: the width of the rectangle
            @height: the height of the rectangle
            @x: x
            @y: y
            @id: id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value o y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
