#!/usr/bin/python3
"""module of 'BaseModel' class"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Representation of a BaseModel"""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """custom __str__ method for BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
           of __dict__ of the instance"""

        dict_ = dict(self.__dict__)
        dict_.update({"__class__": self.__class__.__name__,
                      "created_at": str(((self.created_at).isoformat())),
                      "updated_at": str(((self.updated_at).isoformat()))})
        return dict_
