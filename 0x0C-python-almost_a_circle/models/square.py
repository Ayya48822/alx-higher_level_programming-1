#usr/bin/python3
"""creating a class square that inherits from class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the instance"""
        super().__init__(size, size, x, y, id)
