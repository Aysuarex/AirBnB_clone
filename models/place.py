#!/usr/bin/env python3
"""" Class place """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class place inherits from BaseModel
    Public class attributes:
        city_id: string - (str): City.id
        user_id: string - (str): User.id
        name: (str) - Name of the place
        description: (str) - Description of the place
        number_rooms: (int) - Number of rooms of the place
        number_bathrooms: (int) - Number of bathrooms of the place
        max_guest: (int) - Maximum number of guests that can be accommodated
        price_by_night: (int) - Price per night
        latitude: (float) - Latitude of the place
        longitude: (float) - Longitude of the place
        amenity_ids: (list) - List of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Initialize class Place
            Args:
                *args: list of strings
                **kwargs: dictionary of strings
                """
        super().__init__(*args, **kwargs)
