#!/bin/bash/python3
"""
    Class File Storage
"""

from models.base_model import BaseModel
import json

class FileStorage():
    """Seialises instances to a JSON"""

    #string - path to the JSON file
    __file_path = "file.json"
    #dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not none:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj                
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""



    def reload(self):
        """ deserializes the JSON file to __objects """