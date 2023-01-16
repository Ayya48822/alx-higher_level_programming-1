#usr/bin/python3
"""creating a class square that inherits from class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ __str__ magic method"""
        square = "[Square] "
        square_id = "({}) ".format(self.id)
        square_xy = "{}/{} - ".format(self.x, self.y)
        square_size = "{}".format(self.width)

        return square + square_id + square_xy + square_size

    @property
    def size(self):
        """getting the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setting the value of the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ creating the update function"""
