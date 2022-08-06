#!/usr/bin/env python3
""" class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherits BaseModel
        Public class attribute
            state_id: (str) - State.id
            name: (str) - City name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize City
            Args:
                *args: list of strings
                **kwargs: dictionary of strings"""
        super().__init__(*args, **kwargs)
