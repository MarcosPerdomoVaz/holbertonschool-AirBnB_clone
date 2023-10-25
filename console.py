#!/usr/bin/python3
"""sddfsd dfdf df d f"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class command console"""
    prompt = "(hbnb)"

    class_names = ["BaseModel"]

    def do_quit(self, arg):
        """quit command"""
        return True

    def do_EOF(self, arg):
        """ctr + d"""
        return True

    def do_create(self, arg):
        """sd  f df df  df """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.class_names:
            print("** class doesn't exist **")
        else:
            cr_inst = BaseModel()
            cr_inst.save()
            print(cr_inst.id)

    def do_show(self, arg):
        """sdsdsd s d sdsa dsd """
        arg_list = arg.split(" ")
        if len(arg_list) < 1:
            print("** class name missing **")
        elif arg_list[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instnace id missing **")
        else:
            stored_objs = storage.all()
            if f"{arg_list[0]}.{arg_list[1]}" in stored_objs.keys():
                print(f"{stored_objs[f'{arg_list[0]}.{arg_list[1]}']}")
            else:
                print("** no instance found **")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
