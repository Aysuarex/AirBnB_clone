#!/usr/bin/env python3
"""
Unitest for models/place.py

Unittest classes:
    Test_place_instantiation
    Test_place_save
    Test_place_str
    Test_place_to_dict
    """

import unittest
import os
from datetime import datetime
from time import sleep
from models.place import Place
import models


###############################################################################
# Test_place_instantiation
###############################################################################


class Test_place_instantiation(unittest.TestCase):
    """ test instantiation fo Place class """

    def test_Place_instantiation_no_args(self):
        """ test instantiation without args """
        self.assertEqual(Place, type(Place()))

    def test_Place_instantiation_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_Place_instantiation_id__str(self):
        self.assertEqual(str, type(Place().id))

    def test_Place_instantiation_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_Place_instantiation_updated_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_Place_instantiation_unique_ids(self):
        """test unique ids on two places"""
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_Place_instantiation_created_at(self):
        """ test different created at in two places"""
        pl1 = Place()
        sleep(0.2)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def ttest_Place_instantiation_updated_at(self):
        """ test different updated at in two places """
        pl1 = Place()
        sleep(0.2)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_Place_instantiation_city(self):
        """ test city is public class attribute"""
        plc = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(plc))
        self.assertNotIn("city_id", plc.__dict__)

    def test_Place_instantiation_id(self):
        """ test user id public class attribute """
        plc = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(plc))
        self.assertNotIn("user_id", plc.__dict__)

    def test_Place_instantiation_name(self):
        """ test if name is public class attribute """
        plc = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(plc))
        self.assertNotIn("name", plc.__dict__)

    def test_Place_instantiation_description(self):
        """ test if description is public attribute """
        plc = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(plc))
        self.assertNotIn("desctiption", plc.__dict__)

    def test_Place_instantiation_rooms(self):
        """ test if number of rooms is public attribute"""
        plc = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(plc))
        self.assertNotIn("number_rooms", plc.__dict__)

    def test_Place_instantiation_bathrooms(self):
        """ test if number of bathrooms is public class attribute """
        plc = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(plc))
        self.assertNotIn("number_bathrooms", plc.__dict__)

    def test_Place_instantiation_max_guest(self):
        """ test if max guest is public class attribute"""
        plc = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(plc))
        self.assertNotIn("max_guest", plc.__dict__)

    def test_Place_instantiation_price_(self):
        """ test if price is public class attribute """
        plc = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(plc))
        self.assertNotIn("price_by_night", plc.__dict__)

    def test_Place_instantiation_latitude(self):
        """ test if latitude is public class attribute """
        plc = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(plc))
        self.assertNotIn("latitude", plc.__dict__)

    def test_Place_instantiation_longitude(self):
        """ test if longitude is public class attribute """
        plc = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(plc))
        self.assertNotIn("longitude", plc.__dict__)

    def test_Place_instantiation_amenity(self):
        """ test if amenity is public class attribute """
        plc = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(plc))
        self.assertNotIn("amenity_ids", plc.__dict__)

    def test_Place_instantiation_kwargs_None(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_Place_instantiation_kwargs(self):
        """ instantiates with kwargs """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        plc = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(plc.id, "345")
        self.assertEqual(plc.created_at, dt)
        self.assertEqual(plc.updated_at, dt)

    def test_Place_instantiation_u_args(self):
        """ unused args """
        plc = Place(None)
        self.assertNotIn(None, plc.__dict__.values())

###############################################################################
# Test_place_save
###############################################################################


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "other")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("other", "file.json")
        except IOError:
            pass

    def test_place_save_one(self):
        """ test save one """
        plc = Place()
        sleep(0.1)
        first_updated_at = plc.updated_at
        plc.save()
        self.assertLess(first_updated_at, plc.updated_at)

    def test_place_save_two(self):
        """ test save two times """
        plc = Place()
        sleep(0.1)
        first_updated_at = plc.updated_at
        plc.save()
        second_updated_at = plc.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.1)
        plc.save()
        self.assertLess(second_updated_at, plc.updated_at)

    def test_place_save_arg(self):
        """ save with args"""
        plc = Place()
        with self.assertRaises(TypeError):
            plc.save(None)

    def test_place_save_update(self):
        """ save update"""
        plc = Place()
        plc.save()
        plid = "Place." + plc.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())

###############################################################################
# Test_place_str
###############################################################################


class TestPlace_str(unittest.TestCase):
    def test_place_str_method(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        plc = Place()
        plc.id = "111111111"
        plc.created_at = plc.updated_at = dt
        plstr = plc.__str__()
        self.assertIn("[Place] (111111111)", plstr)
        self.assertIn("'id': '111111111'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

###############################################################################
# Test_place_to_dict
###############################################################################


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_place_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_args(self):
        plc = Place()
        with self.assertRaises(TypeError):
            plc.to_dict(None)

    def test_to_dict_out(self):
        """ test output """
        dt = datetime.today()
        plc = Place()
        plc.id = "121212"
        plc.created_at = plc.updated_at = dt
        tdict = {
            'id': '121212',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(plc.to_dict(), tdict)

    def test_place_to_dict_add_atr(self):
        """ test if contains added ttributes """
        plc = Place()
        plc.middle_name = "Ronald"
        plc.my_number = 41
        self.assertEqual("Ronald", plc.middle_name)
        self.assertIn("my_number", plc.to_dict())

    def test_place_to_dict_keys(self):
        """ test if dict have right keys """
        plc = Place()
        self.assertIn("id", plc.to_dict())
        self.assertIn("created_at", plc.to_dict())
        self.assertIn("updated_at", plc.to_dict())
        self.assertIn("__class__", plc.to_dict())

    def test_to_dict_str_atr(self):
        """ test if attributes are str type """
        plc = Place()
        pl_dict = plc.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_class_atr(self):
        """ test if attributes are str type """
        plc = Place()
        pl_dict = plc.to_dict()
        self.assertEqual("Place", pl_dict["__class__"])

    def test_to_dict_class_atr(self):
        """ test if attributes are str type """
        plc = Place()
        pl_dict = plc.to_dict()
        self.assertEqual("Place", pl_dict["__class__"])


if __name__ == "__main__":
    unittest.main()
