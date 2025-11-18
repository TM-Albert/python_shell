import os
import sys
from tokenizer import ShellTokenizer 
from shell_parser import ShellParser
from shell_builtins import ShellBuiltins

class ShellExecutor:
    """
    ShellExecutor is responsible for executing the shell program
    """

    def __init__(self):
        self.supported_commands = ShellBuiltins().builtin_commands
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
        for i, cmd in enumerate(self.supported_commands.keys(), 1):
            print(f"{i}- {cmd.upper()}")

    def run(self):
        """
        
        """

        while True:
            # Output buffer
            sys.stdout.write("$ ")
            sys.stdout.flush() # forces Python to empty the buffer immediately and write it to the terminal.
            line = sys.stdin.readline()

            if not line.strip():
                continue

            tokenized_line = ShellTokenizer().tokenize(line)

            parser = ShellParser(
                supported=self.supported_commands,
                operators=self.operators,
                redirects=self.redirects
            )

            command_flow = parser.parse(tokenized_line)

            # Execution of the CommandObjects with the help of builtin functions

if __name__ == "__main__":
    se = ShellExecutor()
    se.run()