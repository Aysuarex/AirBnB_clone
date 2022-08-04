#!/usr/bin/python3
"""Defines the BaseModel"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base model for the Airbnb Clone Project
    """

    def __init__(self, *args, **kwargs):
        """
        Basemodel Constructor
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage(save)
        else:
            format = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strftime(kwargs["created_at"], format)
            kwargs["updated_at"] = datetime.strftime(kwargs["updated_at"], format)
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """
        print the instance
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
            updates the public instance attribute
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
