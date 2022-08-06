#!/usr/bin/env python3
"""
Console for object management and storage persistant
"""
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import os
import sys
import json
import cmd
import shlex
""" 6. Console 0.0.1 """

my_classes = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """-HBNBCommand(cmd.Cmd) is a class that inherits from cmd.Cmd
                    cmd.Cmd is methods to execute a command prompt command
                    line interface for a Python program.
       -prompt is a interpreter-specific string that is displayed to the user
       when they are ready to enter a command.
       -classes is a list of all the classes that inherit from BaseModel.
       -my_objects is a dictionary of all the instances of the classes
       in classes.
       -my_classes oa diccionary whit the classes.
       -storage is an instance of FileStorage.
       -self is an instance of HBNBCommand to use the methods of the class.
       -args is a list of arguments passed to the command.
       -args_list is a list of arguments passed to the command."""

    prompt = '(hbnb) '
    classes = ["BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"]

    """reload() reloads the JSON file

    instances = ["do_show", "do_destroy", "do_all", "do_update"]"""

    def do_quit(self, args):
        """Quit command to exit the program.\n"""
        quit()

    def do_EOF(self, args):
        """End Of File command to exit the program"""
        quit()

    def emptyline(self):
        """Do nothing on empty line\n"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel \
saves it (to the JSON file) and prints the id.
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in my_classes:
            print("** class doesn't exist **")
            return
        if args[0] in my_classes:
            """if the args[0] is in my_classes, then the class exists"""
            new_object = eval(args[0])()
            new_object.save()
            """save() saves the changes in the JSON file"""
            print(new_object.id)
            """print the id of the object"""

    def do_show(self, args):
        """Prints the string representation of an instance, format:
        show <class name> <id>."""

        args_list = shlex.split(args)
        """args_list is a list of arguments passed to the command
              shlex is a lexical analyser for simple shell-like syntax;
                and shlex.split() splits a string into a list of tokens."""
        if not args:
            print("** class name missing **")
            return
        elif args_list[0] not in my_classes:
            print("** class doesn't exist **")
            return
        elif len(args_list) == 1:
            print("** instance id missing **")
            return
        new_object = "{}.{}".format(args_list[0], args_list[1])
        """new_object is a string that is the class name an the id"""
        if new_object not in models.storage.all().keys():
            """if the new_object is not in the dictionary,
            then the object doesn't exist"""
            print("** no instance found **")
            return
        else:
            print("[{}] ({}) {}".format(args_list[0], new_object[1],
                  models.storage.all()[new_object]))
            """print the object in format [class name] (id) object"""

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args_list = shlex.split(args)
        """args_list is a list of arguments passed to the command
                shlex is a lexical analyser for simple shell-like syntax;
                and shlex.split() splits a string into a list of tokens."""
        if len(args_list) == 0:
            print("** class name missing **")
            return
        elif args_list[0] in my_classes:
            """if the args_list[0] is in my_classes, then the class exists"""
            if len(args_list) > 1:
                """if the lenght of args_list is greater than 1,
                then the id is passed"""
                key = args_list[0] + "." + args_list[1]
                """key = args_list[0] + "." + args_list[1]
                    key is the key to search in the dictionary"""
                if key in models.storage.all():
                    del models.storage.all()[key]
                    """del(key) removes the key from the dictionary"""
                    models.storage.save()
                    """save() saves the changes in the JSON file"""
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name."""

        new_object = models.storage.all()
        """new_object is a dictionary with all the objects"""
        list_objects = []
        """list_objects is a list with all the objects"""
        if args not in my_classes:
            """if args is not empty and args is not in my_classes,
            then the class doesn't exist"""
            print("** class doesn't exist **")
            return
        if args in self.classes:
            for key, value in new_object.items():
                """for key, value in new_object.items()
                    key is the key of the dictionary
                    value is the value of the dictionary, new_object.items is a
                    generator that returns the key-value of the dictionary"""
                if args in key:
                    """if args is in key, then the class exists"""
                    toke_key = key.split(".")
                    """toke_key is a list with the class name and the id"""
                    key_new = "[" + toke_key[0] + "]"\
                        + " (" + toke_key[1] + ")"
                    list_objects.append(key_new + " " + str(value))
                    """list_objects.append(key_new + " " + str(value))
                        list_objects is a list with the objects in format
                        [class name] (id) object"""
                    print(list_objects)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""

        if args == '':
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        key = args_list[0] + "." + args_list[1]
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args_list) == 2:
            print("** attribute name missing **")
            return
        if len(args_list) == 3:
            print("** value missing **")
            return
        attribute = args_list[2]
        value = args_list[3]
        if '"' in value:
            value = value.strip('"')
        """args_list[0] is the class name, args_list[1] is the id, args_list[2]
        is the attribute name, args_list[3] is the value to update"""
        try:
            setattr(all_objects[key], attribute, value)
            models.storage.save()
        except AttributeError:
            print("** attribute name missing **")
            return

    def do_count(self, args):
        """counts the number of instances of a class"""
        counter = 0
        my_objects = models.storage.all()
        """my_objects is a dictionary with the key and value of the
             dictionary"""
        if args in self.classes:
            for key in my_objects.keys():
                """for key in my_objects.keys() is a loop that
                iterates over the keys of the dictionary"""
                find_class = key.split(".")
                """find_class is a list of the key split by "." """
                if find_class[0] == args:
                    """if find_class[0] == args, then the class name
                    is the same as the args"""
                    counter += 1
                    """counter += 1 is a function that adds 1 to the counter"""
            print(counter)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
