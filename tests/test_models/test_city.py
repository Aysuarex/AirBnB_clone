#!/usr/bin/python3
"""test module for class City"""

import models
import datetime
import unittest


class CityTest(unittest.TestCase):
    """tests the class City"""

    def test_documentation(self):
        """tests module and class docstring"""
        self.assertIsNotNone(models.city.__doc__)
        self.assertIsNotNone(models.city.City.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.city.City()
        self.assertIsInstance(instance, models.city.City)

    def test_type(self):
        """test type of instance atributes"""
        instance = models.city.City()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.state_id, str)
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()
