#!/usr/bin/env python3
"""
Unitest for models/amenity.py

Unittest classes:
    Test_amentity_instantiation
    """
import os
import unittest
import models
from datetime import datetime
from models.amenity import Amenity
from time import sleep


class Test_models_amenity(unittest.TestCase):
    """
        Test_models_amenity class
    """

    def test_instantiation_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_args_unused(self):
        amen1 = Amenity(None)
        self.assertNotIn(None, amen1.__dict__.values())

    def test_instantiation_kwargs(self):
        am_date = datetime.today()
        dt_iso = am_date.isoformat()
        amen1 = Amenity(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amen1.id, "123")
        self.assertEqual(amen1.created_at, am_date)
        self.assertEqual(amen1.updated_at, am_date)

    def test_instantiation_kwargs_none(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_instantiation_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_public_class_attr(self):
        amen1 = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amen1.__dict__)

    def test_two_amenities_ids(self):
        amen1 = Amenity()
        amen2 = Amenity()
        self.assertNotEqual(amen1.id, amen2.id)

    def test_two_amenities_created_at(self):
        amen1 = Amenity()
        sleep(0.1)
        amen2 = Amenity()
        self.assertLess(amen1.created_at, amen2.created_at)

    def test_two_amenities_updated_at(self):
        amen1 = Amenity()
        sleep(0.1)
        amen2 = Amenity()
        self.assertLess(amen1.updated_at, amen2.updated_at)

    def test_amenities_str(self):
        am_date = datetime.today()
        dt_repr = repr(am_date)
        amen1 = Amenity()
        amen1.id = "121212"
        amen1.created_at = amen1.updated_at = am_date
        amstr = amen1.__str__()
        self.assertIn("[Amenity] (121212)", amstr)
        self.assertIn("'id': '121212'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)


if __name__ == '__main__':
    unittest.main()
