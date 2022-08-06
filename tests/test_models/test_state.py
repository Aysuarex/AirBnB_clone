#!/usr/bin/python3
"""test module for class State"""

import models
import datetime
import unittest


class StateTest(unittest.TestCase):
    """tests the class State"""

    def test_documentation(self):
        """tests module and class docstring"""
        self.assertIsNotNone(models.state.__doc__)
        self.assertIsNotNone(models.state.State.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.state.State()
        self.assertIsInstance(instance, models.state.State)

    def test_type(self):
        """test type of instance atributes"""
        instance = models.state.State()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()
