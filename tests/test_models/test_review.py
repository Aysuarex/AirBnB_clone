#!/usr/bin/python3
"""test module for class Review"""

import models
import datetime
import unittest


class ReviewTest(unittest.TestCase):
    """tests the class Review"""

    def test_documentation(self):
        """tests module and class docstring"""
        self.assertIsNotNone(models.review.__doc__)
        self.assertIsNotNone(models.review.Review.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.review.Review()
        self.assertIsInstance(instance, models.review.Review)

    def test_type(self):
        """test type of instance atributes"""
        instance = models.review.Review()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.place_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.text, str)


if __name__ == "__main__":
    unittest.main()
