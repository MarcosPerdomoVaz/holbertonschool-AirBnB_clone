#!/usr/bin/python3
"""Console for holbertonschool-AirBnB_clone"""


import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
           }


class HBNBCommand(cmd.Cmd):
    """
    our cmd loop interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """Quit console at EOF\n"""
        print("")
        return True

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        arg_list = arg.split()
        if len(arg_list) < 1:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            stored_objs = models.storage.all()
            if f"{arg_list[0]}.{arg_list[1]}" in stored_objs.keys():
                print(f"{stored_objs[f'{arg_list[0]}.{arg_list[1]}']}")
            else:
                print("** no instance found **")

    def emptyline(self):
        """No action: input is empty line + ENTER\n"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel saves it (to the JSON file) and prints the id\n"""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif args in classes:
            instance = eval(str(args) + "()")
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")
            return False

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id\n"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arg) < 2:
            print("** instance id missing **")
            return False

        else:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        specifying or not on the class name\n"""
        arg = args.split()
        objList = []
        if len(args) == 0:
            for key in models.storage.all():
                objList.append(str(models.storage.all()[key]))
            print(objList)
        if len(arg) == 1:
            if arg[0] in classes:
                for key in models.storage.all():
                    if arg[0] in key:
                        objList.append(str(models.storage.all()[key]))
                print(objList)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance
        Based on class name and id
        By adding or updating attribute"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        elif len(arg) < 2:
            print("** instance id missing **")
            return False
        elif len(arg) < 3:
            print("** attribute name missing **")
            return False
        elif len(arg) < 4:
            print("** value missing **")
            return False
        elif len(arg) < 5:
            key = arg[0] + "." + arg[1]
            if key in models.storage.all():
                setattr(models.storage.all()[key], arg[2], arg[3].replace('"', ""))
                models.storage.all()[key].save()
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    """our main"""
    HBNBCommand().cmdloop()
