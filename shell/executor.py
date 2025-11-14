import os
import sys

class ShellExecutor:
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
        
        """

        print(self.supported_commands.__doc__)

    def run(self):
        """
        
        """
        pass