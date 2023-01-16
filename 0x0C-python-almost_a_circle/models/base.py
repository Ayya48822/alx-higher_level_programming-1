#!/usr/bin/python3
""" Module for the base model"""
import json

class Base:
    """ initializing the number of object variable"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ creating the init function

        Args:
            @id: the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ a function to json string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
