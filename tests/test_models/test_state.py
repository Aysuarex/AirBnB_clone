#!/usr/bin/env python3
"""
Unitest for models/state.py

Unittest classes:
    test_state_instantiates
    test_state_save
    test_state_dict
    """

import unittest
import models
from models.state import State


class test_state_instantiates(unittest.TestCase):
    """ Unittest for testing instantiation"""

    def test_instantiation(self):
        self.assertIs(State, type(State()))

    def test_instantiation_with_kwargs(self):
        self.assertIs(State, type(State(name="California")))


class test_state_save(unittest.TestCase):
    """ Unittest for testing save"""

    def test_save(self):
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_save_updated(self):
        state = State()
        state.save()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_save_to_json(self):
        state = State()
        state.save()
        self.assertIs(type(state.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
