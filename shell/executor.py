import os
import sys
from tokenizer import ShellTokenizer 
from shell_parser import ShellParser

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

        while True:
            # Output buffer
            sys.stdout.write("$ ")
            sys.stdout.flush() # forces Python to empty the buffer immediately and write it to the terminal.
            input = sys.stdin.readline()

            print(input)

            # tokenized_input = ShellTokenizer().tokenize(input)
            # parsed_input = ShellParser().parse(tokenized_input)

            # Execution of the CommandObjects with the help of builtin functions

if __name__ == "__main__":


    se = ShellExecutor()
    se.run()