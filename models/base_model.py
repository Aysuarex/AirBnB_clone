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

        Public Instance attributes:
         |--------------------------|
          id: string
            assign with an uuid when an instance is created
          created_at: datetime
            assign with the current datetime when an instance is created
          updated_at: datetime
            assign with the current datetime when an instance is created
            and it will be updated every time you change your object
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage(save)
        else:
            fto = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], fto)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], fto)
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
