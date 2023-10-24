#!/usr/bin/python3
"""sddfsd dfdf df d f"""

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()