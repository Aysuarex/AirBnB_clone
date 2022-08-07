#!/usr/bin/python3
"""module of 'Amenity' class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class 'Amenity' that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
