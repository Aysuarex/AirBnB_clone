#!/usr/bin/python3
"""module of 'State' class"""

from models.base_model import BaseModel


class State(BaseModel):
    """class 'State' that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
