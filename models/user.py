#!/usr/bin/env python3
""" Class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class user that inherits from BaseModel
        Public class attributes:
            email: (str) - user's email
            password: (str) - user's password
            first_name: (str) - user's first name
            last_name: (str) - user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize class User
            Args:
                *args: list of strings
                **kwargs: dictionary of strings
                """
        super().__init__(*args, **kwargs)
