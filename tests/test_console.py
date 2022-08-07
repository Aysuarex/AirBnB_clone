#!/usr/bin/python3
"""test module for console.py"""

import os
import unittest
from models import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """tests the HBNB command interpreter"""

    def test_emptyline(self):
        HBNBCommand().onecmd("")

    def test_do_quit(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_do_EOF(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_errors(unittest.TestCase):
    """tests the HBNB command interpreter"""

    """create command"""
    def test_create_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_create_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    """show command"""
    def test_show_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_show_invalid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show BaseModel 121212")
            self.assertEqual(expected, obtained.getvalue().strip())

    """destroy command"""
    def test_destroy_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_destroy_invalid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            self.assertEqual(expected, obtained.getvalue().strip())

    """all command"""
    def test_all_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    """update command"""
    def test_update_missing_class(self):
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_invalid_class(self):
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_id(self):
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_invalid_id(self):
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("update BaseModel 121212")
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_attribute(self):
        expected = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = "update BaseModel {}".format(id)
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertEqual(expected, obtained.getvalue().strip())

    def test_update_missing_value(self):
        expected = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = "update BaseModel {} first_name".format(id)
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertEqual(expected, obtained.getvalue().strip())


class TestHBNBCommand_all_method(unittest.TestCase):
    """tests the HBNB command interpreter"""

    @classmethod
    def create_all_classes(self):
        HBNBCommand().onecmd("create BaseModel")
        HBNBCommand().onecmd("create User")
        HBNBCommand().onecmd("create State")
        HBNBCommand().onecmd("create City")
        HBNBCommand().onecmd("create Amenity")
        HBNBCommand().onecmd("create Place")
        HBNBCommand().onecmd("create Review")

    def test_all_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.create_all_classes()
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())

    def test_all_User(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.create_all_classes()
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("User.all()")
            self.assertIn("User", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())

    def test_all_State(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.create_all_classes()
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("State.all()")
            self.assertIn("State", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())

    def test_all_City(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.create_all_classes()
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("City.all()")
            self.assertIn("City", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())

    def test_all_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.create_all_classes()
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Amenity.all()")
            self.assertIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())

    def test_all_Place(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.create_all_classes()
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Place.all()")
            self.assertIn("Place", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Review", obtained.getvalue().strip())

    def test_all_Review(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            self.create_all_classes()
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Review.all()")
            self.assertIn("Review", obtained.getvalue().strip())
            self.assertNotIn("BaseModel", obtained.getvalue().strip())
            self.assertNotIn("User", obtained.getvalue().strip())
            self.assertNotIn("State", obtained.getvalue().strip())
            self.assertNotIn("City", obtained.getvalue().strip())
            self.assertNotIn("Amenity", obtained.getvalue().strip())
            self.assertNotIn("Place", obtained.getvalue().strip())


class TestHBNBCommand_all_method(unittest.TestCase):
    """tests the HBNB command interpreter"""

    def test_show_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = 'BaseModel.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())

    def test_show_User(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create User")
            id = obtained.getvalue().strip()
            command = 'User.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())

    def test_show_State(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create State")
            id = obtained.getvalue().strip()
            command = 'State.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())

    def test_show_City(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create City")
            id = obtained.getvalue().strip()
            command = 'City.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())

    def test_show_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Amenity")
            id = obtained.getvalue().strip()
            command = 'Amenity.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())

    def test_show_Place(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Place")
            id = obtained.getvalue().strip()
            command = 'Place.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())

    def test_show_Review(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Review")
            id = obtained.getvalue().strip()
            command = 'Review.show("' + obtained.getvalue().strip() + '")'
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd(command)
            self.assertIn(id, obtained.getvalue().strip())


class TestHBNBCommand_all_method(unittest.TestCase):
    """tests the HBNB command interpreter"""

    def test_destroy_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            instance = 'BaseModel.' + obtained.getvalue().strip()
            shortcut = obtained.getvalue().strip()
            command = 'BaseModel.destroy("{}")'.format(shortcut)
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())

    def test_destroy_User(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create User")
            instance = 'User.' + obtained.getvalue().strip()
            shortcut = obtained.getvalue().strip()
            command = 'User.destroy("{}")'.format(shortcut)
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())

    def test_destroy_State(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create State")
            instance = 'State.' + obtained.getvalue().strip()
            shortcut = obtained.getvalue().strip()
            command = 'State.destroy("{}")'.format(shortcut)
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())

    def test_destroy_City(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create City")
            instance = 'City.' + obtained.getvalue().strip()
            shortcut = obtained.getvalue().strip()
            command = 'City.destroy("{}")'.format(shortcut)
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())

    def test_destroy_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Amenity")
            instance = 'Amenity.' + obtained.getvalue().strip()
            shortcut = obtained.getvalue().strip()
            command = 'Amenity.destroy("{}")'.format(shortcut)
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())

    def test_destroy_Place(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Place")
            instance = 'Place.' + obtained.getvalue().strip()
            shortcut = obtained.getvalue().strip()
            command = 'Place.destroy("{}")'.format(shortcut)
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())

    def test_destroy_Review(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Review")
            instance = 'Review.' + obtained.getvalue().strip()
            shortcut = obtained.getvalue().strip()
            command = 'Review.destroy("{}")'.format(shortcut)
            self.assertIn(instance, storage.all().keys())
            HBNBCommand().onecmd(command)
            self.assertNotIn(instance, storage.all().keys())


class TestHBNBCommand_all_method(unittest.TestCase):
    """tests the HBNB command interpreter"""

    def test_update_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = 'BaseModel.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            comand = 'BaseModel.update("{}", "Holberton", "School")'.format(id)
            HBNBCommand().onecmd(comand)
            command = 'BaseModel.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())

    def test_update_User(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create User")
            id = obtained.getvalue().strip()
            command = 'User.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            command = 'User.update("{}", "Holberton", "School")'.format(id)
            HBNBCommand().onecmd(command)
            command = 'User.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())

    def test_update_State(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create State")
            id = obtained.getvalue().strip()
            command = 'State.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            command = 'State.update("{}", "Holberton", "School")'.format(id)
            HBNBCommand().onecmd(command)
            command = 'State.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())

    def test_update_City(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create City")
            id = obtained.getvalue().strip()
            command = 'City.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            command = 'City.update("{}", "Holberton", "School")'.format(id)
            HBNBCommand().onecmd(command)
            command = 'City.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())

    def test_update_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Amenity")
            id = obtained.getvalue().strip()
            command = 'Amenity.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            command = 'Amenity.update("{}", "Holberton", "School")'.format(id)
            HBNBCommand().onecmd(command)
            command = 'Amenity.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())

    def test_update_Place(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Place")
            id = obtained.getvalue().strip()
            command = 'Place.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            command = 'Place.update("{}", "Holberton", "School")'.format(id)
            HBNBCommand().onecmd(command)
            command = 'Place.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())

    def test_update_Review(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Review")
            id = obtained.getvalue().strip()
            command = 'Review.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            command = 'Review.update("{}", "Holberton", "School")'.format(id)
            HBNBCommand().onecmd(command)
            command = 'Review.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())


class TestHBNBCommand_all_method(unittest.TestCase):
    """tests the HBNB command interpreter"""

    def test_update_dict_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            id = obtained.getvalue().strip()
            command = 'BaseModel.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            self.assertNotIn("Montevideo", obtained.getvalue().strip())
            self.assertNotIn("Uruguay", obtained.getvalue().strip())
            shortcut = '{ "Holberton": "School", "Montevideo": "Uruguay" }'
            command = 'BaseModel.update("{}", {})'.format(id, shortcut)
            HBNBCommand().onecmd(command)
            command = 'BaseModel.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())
            self.assertIn("Montevideo", obtained.getvalue().strip())
            self.assertIn("Uruguay", obtained.getvalue().strip())

    def test_update_dict_User(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create User")
            id = obtained.getvalue().strip()
            command = 'User.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            self.assertNotIn("Montevideo", obtained.getvalue().strip())
            self.assertNotIn("Uruguay", obtained.getvalue().strip())
            shortcut = '{ "Holberton": "School", "Montevideo": "Uruguay" }'
            command = 'User.update("{}", {})'.format(id, shortcut)
            HBNBCommand().onecmd(command)
            command = 'User.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())
            self.assertIn("Montevideo", obtained.getvalue().strip())
            self.assertIn("Uruguay", obtained.getvalue().strip())

    def test_update_dict_State(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create State")
            id = obtained.getvalue().strip()
            command = 'State.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            self.assertNotIn("Montevideo", obtained.getvalue().strip())
            self.assertNotIn("Uruguay", obtained.getvalue().strip())
            shortcut = '{ "Holberton": "School", "Montevideo": "Uruguay" }'
            command = 'State.update("{}", {})'.format(id, shortcut)
            HBNBCommand().onecmd(command)
            command = 'State.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())
            self.assertIn("Montevideo", obtained.getvalue().strip())
            self.assertIn("Uruguay", obtained.getvalue().strip())

    def test_update_dict_City(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create City")
            id = obtained.getvalue().strip()
            command = 'City.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            self.assertNotIn("Montevideo", obtained.getvalue().strip())
            self.assertNotIn("Uruguay", obtained.getvalue().strip())
            shortcut = '{ "Holberton": "School", "Montevideo": "Uruguay" }'
            command = 'City.update("{}", {})'.format(id, shortcut)
            HBNBCommand().onecmd(command)
            command = 'City.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())
            self.assertIn("Montevideo", obtained.getvalue().strip())
            self.assertIn("Uruguay", obtained.getvalue().strip())

    def test_update_dict_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Amenity")
            id = obtained.getvalue().strip()
            command = 'Amenity.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            self.assertNotIn("Montevideo", obtained.getvalue().strip())
            self.assertNotIn("Uruguay", obtained.getvalue().strip())
            shortcut = '{ "Holberton": "School", "Montevideo": "Uruguay" }'
            command = 'Amenity.update("{}", {})'.format(id, shortcut)
            HBNBCommand().onecmd(command)
            command = 'Amenity.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())
            self.assertIn("Montevideo", obtained.getvalue().strip())
            self.assertIn("Uruguay", obtained.getvalue().strip())

    def test_update_dict_Place(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Place")
            id = obtained.getvalue().strip()
            command = 'Place.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            self.assertNotIn("Montevideo", obtained.getvalue().strip())
            self.assertNotIn("Uruguay", obtained.getvalue().strip())
            shortcut = '{ "Holberton": "School", "Montevideo": "Uruguay" }'
            command = 'Place.update("{}", {})'.format(id, shortcut)
            HBNBCommand().onecmd(command)
            command = 'Place.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())
            self.assertIn("Montevideo", obtained.getvalue().strip())
            self.assertIn("Uruguay", obtained.getvalue().strip())

    def test_update_dict_Review(self):
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create Review")
            id = obtained.getvalue().strip()
            command = 'Review.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertNotIn("Holberton", obtained.getvalue().strip())
            self.assertNotIn("School", obtained.getvalue().strip())
            self.assertNotIn("Montevideo", obtained.getvalue().strip())
            self.assertNotIn("Uruguay", obtained.getvalue().strip())
            shortcut = '{ "Holberton": "School", "Montevideo": "Uruguay" }'
            command = 'Review.update("{}", {})'.format(id, shortcut)
            HBNBCommand().onecmd(command)
            command = 'Review.show("{}")'.format(id)
            HBNBCommand().onecmd(command)
            self.assertIn("Holberton", obtained.getvalue().strip())
            self.assertIn("School", obtained.getvalue().strip())
            self.assertIn("Montevideo", obtained.getvalue().strip())
            self.assertIn("Uruguay", obtained.getvalue().strip())


class TestHBNBCommand_all_method(unittest.TestCase):
    """tests the HBNB command interpreter"""

    def test_count(self):
        try:
            os.remove("file.json")
        except:
            pass
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Place")
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual("3", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual("1", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual("1", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual("2", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual("1", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual("1", obtained.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual("0", obtained.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
