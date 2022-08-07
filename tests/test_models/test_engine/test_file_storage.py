#!/usr/bin/python3
"""test module for class FileStorage"""

import models
import datetime
import unittest
import os


class FileStorageTest(unittest.TestCase):
    """tests the class FileStorage"""

    def test_documentation(self):
        """tests module, class and methods docstring"""
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.__doc__)
        shortcut = models.engine.file_storage.FileStorage
        self.assertIsNotNone(shortcut.__init__.__doc__)
        self.assertIsNotNone(shortcut.all.__doc__)
        self.assertIsNotNone(shortcut.new.__doc__)
        self.assertIsNotNone(shortcut.save.__doc__)
        self.assertIsNotNone(shortcut.reload.__doc__)

    def test_class(self):
        """test instance class"""
        instance = models.engine.file_storage.FileStorage()
        self.assertIsInstance(instance, models.engine.file_storage.FileStorage)

    def test_all(self):
        """test all method"""
        instance = models.engine.file_storage.FileStorage()
        dictionary = instance.all()
        self.assertIsNotNone(dictionary)
        self.assertIsInstance(dictionary, dict)
        self.assertIs(dictionary, instance._FileStorage__objects)

    def test_new(self):
        """test new method"""
        dict1 = models.storage.all().copy()
        instance = models.base_model.BaseModel()
        dict2 = models.storage.all().copy()
        self.assertLess(len(dict1), len(dict2))

    def test_save(self):
        """test save method"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))
        instance = models.base_model.BaseModel()
        instance.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """test reload method"""
        instance = models.engine.file_storage.FileStorage()
        dic1 = models.storage.all().copy()
        models.storage.reload()
        dic2 = models.storage.all().copy()
        self.assertEqual(len(dic1), len(dic2))
        instance.save()
        self.assertIsInstance(instance._FileStorage__file_path, str)
        self.assertIsInstance(instance._FileStorage__objects, dict)
        self.assertTrue(os.path.exists("file.json"))


if __name__ == "__main__":
    unittest.main()
