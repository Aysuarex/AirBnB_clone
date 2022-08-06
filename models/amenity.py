#!/usr/bin/env python3
""" Class Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity that inherits BaseModel
        Public class attribute
            name: (str) - amenity name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize Amenity
            Args:
                *args: list of strings
                **kwargs: dictionary of strings
        """
        super().__init__(*args, **kwargs)
