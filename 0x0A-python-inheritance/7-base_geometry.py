#!/usr/bin/python3
"""
a class BaseGeometry
"""


class BaseGeometry:
    """ a public instance method area"""
    def area(self):
        raise Exception("area() is not implemented")

    """ integer validator"""
    def integer_validator(self, name, value):
        """ intager validator

        Args:
            name (sring): a string
            value (int): the intager value
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
