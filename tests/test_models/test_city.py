#!/usr/bin/env python3
"""
unittests for the City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class testfile(unittest.TestCase):
    """ unittests for City class """
    def test_inheritance(self):
        """ checks if it inherits from BaseModel """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """ checks if it has the correct attributes """
        self.assertTrue('state_id' in City.__dict__)
        self.assertTrue('name' in City.__dict__)

    def test_str(self):
        """ checks if the str method works """
        my_city = City()
        string = "[City] ({}) {}".format(my_city.id, my_city.__dict__)
        self.assertEqual(string, str(my_city))

    def test_save(self):
        """ checks if the save method works """
        my_city = City()
        my_city.save()
        self.assertNotEqual(my_city.created_at, my_city.updated_at)

    def test_to_dict(self):
        """ checks if the to_dict method works """
        my_city = City()
        new_dict = my_city.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(my_city))

    def test_docstring(self):
        """ checks if the docstring is correct """
        self.assertIsNotNone(City.__doc__)


if __name__ == "__main__":
    unittest.main()
