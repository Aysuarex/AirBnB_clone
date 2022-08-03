#!/usr/bin/python3
"""Defines the BaseModel"""
import models


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
