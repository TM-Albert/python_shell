import os
import sys

class ShellExecutor:
    """
    ShellExecutor is responsible for executing the shell program
    """

    def __init__(self):
        self.supported_commands = {
            "exit": None,
            "echo": None,
            "type": None,
            "pwd": None,
            "cd": None
        }

        self.operators = {
            "&&",
            ";",
            "||",
            "|"
        }

        self.redirects = {
            ">": "stdout_redirect",
            "<": "stdin_redirect"
        }

        self.PATH = os.environ["PATH"].split(":")

    def supported_commands(self):
        """
        Returns a list of currently supported shell commands.
        """
        for i, cmd in enumerate(self.commands.keys(), 1):
            print(f"{i}- {cmd.upper()}")

    def run(self):
        """
        
        """
        pass