import sys
import os
import subprocess

class Shell:
    def __init__(self):
        self.commands = {
            "exit": self.cmd_exit,
            "echo": self.cmd_echo,
            "type": self.cmd_type,
            "pwd": self.cmd_pwd
        }
        self.PATH = os.environ["PATH"].split(":")

    def run(self):
        while True:
            sys.stdout.write("$ ")
            user_input = input().strip()

            if not user_input:
                continue

            parts = user_input.split()
            command, args = parts[0], parts[1:]

            handler = self.commands.get(command, self.cmd_not_found)
            should_exit = handler(command, args)

            if should_exit:
                break

    # ----------------------
    # Command Implementations
    # ----------------------

    def cmd_exit(self, *_):
        """Exits the program"""
        return True

    def cmd_echo(self, _cmd, args):
        """Echo back user arguments."""
        print(" ".join(args))

    def cmd_type(self, _cmd, args):
        """Show if a command is builtin."""

        command = args[0]

        if command in self.commands:
            print(f"{command} is a shell builtin")
        else:
            executable_path = self.find_executable_in_path(command)

            if executable_path is None:
                self.cmd_not_found(command)

            else:
                print(f"{command} is {executable_path}")

    def cmd_pwd(self, _cmd, _args):
        """Displays current working directory."""
        print(os.getcwd())
            
    def cmd_not_found(self, cmd, args=None):
        """Handle unknown commands."""

        executable_path = self.find_executable_in_path(cmd)

        if executable_path is None:
            print(f"{cmd}: not found")
            return

        subprocess.run([cmd, *args])
        return

    def find_executable_in_path(self, executable_file_name):
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

if __name__ == "__main__":
    Shell().run()
