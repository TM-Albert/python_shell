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

        self.PATH = os.environ["PATH"].split(":")

    def _find_executable_in_path(self, executable_file_name):
        """
        Search directories listed in the PATH environment variable for an executable file.

        Args:
            cmd_name (str): Name of the executable to locate.

        Returns:
            str | None: Full path to the executable if found and executable, otherwise None.
        """
        found_potencial_file = False
        potential_path = None

        for folder_path in self.PATH:
            potential_path = os.path.join(folder_path, executable_file_name)

            if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
                found_potencial_file = True
                break

        if found_potencial_file:
            return potential_path
        
        return None

    def cmd_exit(self, *_):
        """Exits the program"""
        return True

    def cmd_echo(self, _cmd, args):
        """Echo back user arguments."""
        print(" ".join(args))

    def cmd_type(self):
        """Show if a command is builtin."""
        pass

    def cmd_pwd(self):
        """Displays current working directory."""
        print(os.getcwd())

    def cmd_cd(self):
        """
        
        """
        pass

    def cmd_cat(self, cmd, args):
        """
        
        """
        pass

    def cmd_not_found(self, cmd, args=None):
        """Handle unknown commands."""

        executable_path = self._find_executable_in_path(cmd)

        if executable_path is None:
            print(f"{cmd}: not found")
            return

        subprocess.run([cmd, *args])
        return
        


if __name__ == "__main__":
    c = ShellBuiltins()
    print(c.builtin_commands)