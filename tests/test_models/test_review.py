#!/usr/bin/env python3
"""
Unitest for models/review.py

Unittest classes:
    Test_review_instantiation
    Test_review_save
    Test_review_str
    Test_review_to_dict
    """

import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.review import Review

###############################################################################
# Test_review_instantiation
###############################################################################


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_review_instantiation_no_args_instantiates(self):
        """instantiates without argas"""
        self.assertEqual(Review, type(Review()))

    def test_instantiation_kwargs_None(self):
        """ pass None kwargs"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_review_instantiation_args2(self):
        """ test unused argas"""
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_review_instantiation_instantiation_kwargs(self):
        """ use kwargs """
        dtt = datetime.today()
        dt_iso = dtt.isoformat()
        rev = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rev.id, "345")
        self.assertEqual(rev.created_at, dtt)
        self.assertEqual(rev.updated_at, dtt)

    def test_review_instantiation_new_instance_stored_in_objects(self):
        """ new instance stored in objects"""
        self.assertIn(Review(), models.storage.all().values())

    def test_review_instantiation_id(self):
        """ test if id is public attribute """
        self.assertEqual(str, type(Review().id))

    def test_review_instantiation_created(self):
        """ test if created at is public attribute"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_review_instantiation_updated(self):
        """ tst if updated is public datetime """
        self.assertEqual(datetime, type(Review().updated_at))

    def test_review_instantiation_review_id(self):
        """ test if id is public class atribute"""
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_review_instantiation_user_id(self):
        """ test if user id is public class attribute """
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_review_instantiation_text(self):
        """ test if text is public class attribute"""
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_review_instantiation_ids(self):
        """ test unique ids for two reviews"""
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_review_instantiation_reviews(self):
        """ test two reviews different created at"""
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_review_instantiation_reviews_2(self):
        """ test two reviews different updated"""
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)


###############################################################################
# Test_review_save
###############################################################################


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_review_save_1(self):
        """one save"""
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        self.assertLess(first_updated_at, rev.updated_at)

    def test_review_save_2(self):
        """ saves two times """
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        second_updated_at = rev.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rev.save()
        self.assertLess(second_updated_at, rev.updated_at)

    def test_review_save_save_args(self):
        """ save with args"""
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_review_save_files(self):
        """ update file """
        rev = Review()
        rev.save()
        rvid = "Review." + rev.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


###############################################################################
# Test_review_str
###############################################################################


class Test_review_str(unittest.TestCase):
    def test_review_str_(self):
        """ test review __str__ representation """
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

###############################################################################
# Test_review_to_dict
###############################################################################


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_review_to_dict(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_review_to_dict_args(self):
        """ pass args"""
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)

    def test_review_to_dict_datetime(self):
        """ test datetime atributes as str"""
        rev = Review()
        rv_dict = rev.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_review_to_dict_output(self):
        """ test output"""
        dtt = datetime.today()
        rev = Review()
        rev.id = "121212"
        rev.created_at = rev.updated_at = dtt
        tdict = {
            'id': '121212',
            '__class__': 'Review',
            'created_at': dtt.isoformat(),
            'updated_at': dtt.isoformat(),
        }
        self.assertDictEqual(rev.to_dict(), tdict)

    def test_review_to_dict_keys(self):
        """ test correct key"""
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_review_to_dict_attr(self):
        """ test added attributes """
        rev = Review()
        rev.middle_name = "Holberton"
        rev.my_number = 98
        self.assertEqual("Holberton", rev.middle_name)
        self.assertIn("my_number", rev.to_dict())

    def test_review_to_dict_attr_2(self):
        """ test added attributes """
        rev = Review()
        rev.middle_name = "Holberton"
        rev.my_number = 98
        self.assertEqual(98, rev.my_number)
        self.assertIn("my_number", rev.to_dict())


if __name__ == "__main__":
    unittest.main()
