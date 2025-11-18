import os
import sys
import subprocess

class ShellBuiltins:
    """
    ShellBuiltins contains all builtin command methods
    """

    def __init__(self):
        """
        Auto-register every builtin command.

        Rule (non-negotiable):
        A method is a builtin **iff** its name starts with ``cmd_``.
        The exposed command name is the part after the prefix.

        Examples
        --------
        cmd_echo  →  users type ``echo``
        cmd_ls    →  users type ``ls``

        Adding a new builtin is a single step:
        1. Add a method called cmd_<command_name> to this class.
        2. Nothing else.

        The one-liner below builds the lookup table once, at start-up,
        so the runtime cost is zero and the human cost is minimal.
        """
        self.builtin_commands = {
            name[4:]: getattr(self, name)
            for name in dir(self) if name.startswith('cmd_')
        }

    def cmd_exit(self, *_):
        """Exits the program"""
        return True

    def cmd_echo(self):
        """
        
        """
        pass

    def cmd_type(self):
        """
        
        """
        pass

    def cmd_pwd(self):
        """Displays current working directory."""
        print(os.getcwd())

    def cmd_cd(self):
        """
        
        """
        pass

    def cmd_cat(self):
        """
        
        """
        pass

    def cmd_not_found(self):
        """
        
        """
        pass


if __name__ == "__main__":
    c = ShellBuiltins()
    print(c.builtin_commands)