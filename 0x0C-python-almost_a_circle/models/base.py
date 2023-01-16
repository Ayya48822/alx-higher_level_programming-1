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

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file functions"""
        filename = "{}.json".format(cls.__name__)
        list_dict = []
        
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dict)

        with open(filename, 'w', encoding="utf-8") as my_file:
            my_file.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """return list from json string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creating the create method"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = (10)
        new.update(**dictionary)
        return new
