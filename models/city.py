#!/usr/bin/python3
"""module of 'City' class"""

from models.base_model import BaseModel


class City(BaseModel):
    """class 'City' that inherits from BaseModel"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
