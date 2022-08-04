#!/usr/bin/python3
"""
Class FileStorage
"""

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

attri = {"BaseModel": BaseModel, "City": City, "State": State,
        "Amenity": Amenity, "User": User, "Place": Place, "Review": Review}


class FileStorage():
    """that serializes instances to a JSON"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_ob = {}
        for key in self.__objects:
            json_ob[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_ob, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as first:
                beer = json.load(burger)
            for malta in beer:
                self.__objects[malta] = attri[beer[malta]["__class__"]](
                    **beer[malta])
        except:
            pass
