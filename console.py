#!/bin/bash/python3
"""Entry point of the command interpreter"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class_list = {"BaseModel": BaseModel,
              "City": City,
              "State": State,
              "Amenity": Amenity, 
              "User": User, 
              "Place": Place, 
              "Review": Review
              }


class HBNBCommand(cmd.Cmd):
    """Class definition"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
        
    def do_EOF(self, arg):
        """Exit console"""
        return True

    def emptyline(self):
        """shouldnt execute anything"""
        return False

    def do_create(self, arg):
        """Create a new instances of the class"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_list:
            an_instance = class_list[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(an_instance.id)
        an_instance.save()

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_list:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
                    return False
            else:
                print("** instance id missing **")
                return False
        else:
            print("** class doesn't exist **")
            return False

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_list:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
                    return False
            else:
                print("** instance id missing **")
                return False
        else:
            print("** class doesn't exist **")
            return False




if __name__ == '__main__':
    HBNBCommand().cmdloop()