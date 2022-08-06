#!/usr/bin/env python3
"""
Unit tests for console.py
Unittest classes:
    Test_console_prompt
    Test_console_exit
    Test_console_help
    Test_console_create
    Test_console_show
    Test_console_destroy
    Test_console_all
    Test_console_update
    Test_console_count
    """

from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch
from models import storage

###############################################################################
# prompt
###############################################################################


class Test_console_prompt(unittest.TestCase):
    """test prompting of the command interpreter"""
    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_ine(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

###############################################################################
# exit
###############################################################################


class Test_console_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_exit_exit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            pass

    def test_exit_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            pass

###############################################################################
# help
###############################################################################


class Test_Console_help(unittest.TestCase):
    """test help command"""
    def test_help_quit(self):
        help = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_EOF(self):
        help = "End Of File command to exit the program"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_create(self):
        help = ("Creates a new instance of BaseModel "
                "saves it (to the JSON file) and prints the id.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_all(self):
        help = ("Prints all string representation of all instances\n        "
                "based or not on the class name.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_show(self):
        help = ("Prints the string representation of an instance,"
                " format:\n        "
                "show <class name> <id>.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_destroy(self):
        help = ("Deletes an instance based on the class name and id.")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_count(self):
        help = ("counts the number of instances of a class")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help_update(self):
        help = ("Updates an instance based on the class"
                " name and id by adding or\n        "
                "updating attribute (save the change into the JSON file).")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(help, f.getvalue().strip())

    def test_help(self):
        help = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help, f.getvalue().strip())

    def test_cmd(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

    def test_get_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertEqual("", f.getvalue().strip())

    def test_get_class_wrong(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all "))
            self.assertEqual("", f.getvalue().strip())

###############################################################################
# commands
###############################################################################

    def test_commandobject(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())



if __name__ == "__main__":
    unittest.main()
