#!/usr/bin/env python3
""" Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Public class attributes:

    place_id: string - (str): Place.id
    user_id: string - (str): User.id
    text: string - (str): text of the review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initialize a Review instance
            Args:
                *args: list of strings
                **kwargs: dictionary of strings
        """
        super().__init__(*args, **kwargs)
