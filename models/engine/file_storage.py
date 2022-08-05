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

class_list = {"BaseModel": BaseModel, 
              "City": City, 
              "State": State,
              "Amenity": Amenity,
              "User": User,
              "Place": Place,
              "Review": Review
              }

class FileStorage():
    """Serializes instances to a JSON"""

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
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                a_dict = json.load(f)
            for key in a_dict:
                self.__objects[key] = class_list[a_dict[key]["__class__"]](**a_dict[key])
        except:
            pass
