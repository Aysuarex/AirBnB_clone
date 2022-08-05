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
                instance = args[0] + "." + args[1]
                if instance in models.storage.all():
                    print(models.storage.all()[instance])
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
                instance = args[0] + "." + args[1]
                if instance in models.storage.all():
                    models.storage.all().pop(instance)
                    models.storage.save()
                else:
                    print("** no instance found **")
                    return False
            else:
                print("** instance id missing **")
                return False
        else:
            print("** class doesn't exist **")
            return False

    def do_all(self, arg):
            """Prints string representations of instances"""
            args = shlex.split(arg)
            a_list = []
            if len(args) == 0:
                for value in models.storage.all().values():
                    a_list.append(str(value))
                print("[", end="")
                print(", ".join(a_list), end="")
                print("]")
            elif args[0] in class_list:
                for instance in models.storage.all():
                    if args[0] in instance:
                        a_list.append(str(models.storage.all()[instance]))
                print("[", end="")
                print(", ".join(a_list), end="")
                print("]")
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in tom:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()

