#!/usr/bin/python3
"""sddfsd dfdf df d f"""

import cmd
import sys
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """class command console"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """quit command"""
        return True

    def do_EOF(self,arg):
        """ctr + d"""
        return True

    def emptyline(self):
        pass

        def do_create(self, args):
            """Creates a new instance of BaseModel"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arg) > 1:
            print("Incorrect number of arguments")
            return False
        instance = eval(str(args) + "()")
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            print("Incorrect number of arguments")
            return False
        key = arg[0] + "." + arg[1]
        storage = models.storage.all()
        if key in storage:
            print(storage[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        arg = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if len(arg) > 2:
            print("Incorrect number of arguments")
            return False
        key = arg[0] + "." + arg[1]
        storage = models.storage.all()
        if key in storage:
            del(storage[key])
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        Based or not on the class name"""
        arg = args.split()
        objList = []
        if len(args) == 0:
            for key in models.storage.all():
                objList.append(str(models.storage.all()[key]))
            print(objList)
        if len(arg) == 1:
            if arg[0] in classes:
                storage = models.storage.all()
                for key in storage:
                    if arg[0] in key:
                        objList.append(str(storage[key]))
                print(objList)
            else:
                print("** class doesn't exist **")
        if len(arg) > 1:
            print("Incorrect number of arguments")
            return False

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
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            print("** value missing **")
            return False
        if len(arg) > 4:
            print("Incorrect number of arguments")
            return False
        key = arg[0] + "." + arg[1]
        storage = models.storage.all()
        arg[3] = arg[3].strip('\"')
        argCheck = arg[3].replace(".", "")
        if arg[3].isdigit():
            arg[3] = int(arg[3])
        elif argCheck.isdigit():
            arg[3] = float(arg[3])
        if key in storage:
            setattr(storage[key], arg[2], arg[3])
            models.storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()