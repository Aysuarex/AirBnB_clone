#!/usr/bin/python3
"""module of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_list = {"BaseModel": BaseModel,
              "User": User,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Place": Place,
              "Review": Review
              }
white_list = []
for key in class_list:
    white_list.append(key)
commands = ["do_show",
            "do_destroy",
            "do_all",
            "do_update",
            "do_count"
            ]


class HBNBCommand(cmd.Cmd):
    """Representation of a HBNBCommand"""

    prompt = "(hbnb) "

    def emptyline(self):
        return False

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def do_create(self, line):
        """creates a new instance of BaseModel, saves it and prints the id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        else:
            for key, value in class_list.items():
                if args[0] == key:
                    new_instance = value()
                    print(new_instance.id)
                    new_instance.save()

    def do_show(self, line):
        """prints the string representation of an instance
           based on the class name and id"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] in objects_dic:
            print(objects_dic[args[0]+"."+args[1]])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance based on the class name and id"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] in objects_dic:
            storage.all().pop(args[0]+"."+args[1])
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """prints all string representation of all instances
           based (or not) on the class name"""
        args = line.split()
        objects_dic = storage.all()
        objects_list = []
        if len(args) == 0:
            for key in objects_dic:
                objects_list.append(objects_dic[key].__str__())
            print(objects_list)
        elif args[0] in white_list:
            for key in objects_dic:
                if objects_dic[key].__class__.__name__ == args[0]:
                    objects_list.append(objects_dic[key].__str__())
            print(objects_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """updates an instance based on the class name and id
           by adding or updating attribute"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] not in objects_dic:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0]+"."+args[1]
            attr = args[2]
            value = args[3].replace('"', ' ')
            inst = objects_dic[key]
            if hasattr(inst, attr) and type(getattr(inst, attr)) is int:
                if (value).isnumeric():
                    value = int(value)
            elif hasattr(inst, attr) and type(getattr(inst, attr)) is float:
                idk = args[3].split(".")
                if idk[0].isnumeric() and idk[1].isnumeric():
                    value = float(value)
            setattr(storage.all()[key], attr, value)
            storage.all()[key].save()

    def do_count(self, line):
        """retrieve the number of instances of a class"""
        args = line.split()
        objects_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in white_list:
            print("** class doesn't exist **")
        pichu = 0
        for i in objects_dic:
            if objects_dic[i].__class__.__name__ == args[0]:
                pichu += 1
        print(pichu)

    def default(self, line):
        """default method to use with command()"""
        line = line.replace('(', ' ').replace(')', ' ').replace('.', ' ')
        line = line.replace(',', '').replace("'", '').replace('"', '')
        args = line.split(" ")
        args.remove("")
        if len(args) > 1:
            cmd = args[1]
            args.remove(cmd)
        if cmd == "update":
            if "{" in line:
                line = line.replace('{', '').replace('}', '').replace(':', '')
                args = line.split(" ")
                args.remove("")
                static = args[0] + " " + args[2]
                while len(args) >= 5:
                    variable = args[3] + " " + args[4]
                    args.remove(args[3])
                    args.remove(args[3])
                    argument = static + " " + variable
                    eval('self.do_update' + '(argument)')
                return
        argument = ""
        for arg in args:
            argument = argument + arg + " "
        try:
            eval('self.do_' + cmd + '(argument)')
        except:
            print("** invalid command **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
