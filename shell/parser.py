import os
import sys
from executor import ShellExecutor

class ShellParser:
    """
    ShellParser is responsible for getting the tokenized commands and 
    parsing it to the CommandTree data type which is a Tree based data type
    representing the program flow.
    """

    def __init__(self):
        self.supported_commands = ShellExecutor().supported_commands
        self.operators = ShellExecutor().operators
        self.redirects = ShellExecutor().redirects

    def parse(self, tokenized_commands: list[str]):
        """Parses tokenized commands provided by user from the console.

        Args:
            list[str]: List of shell-compatible tokens.

        Returns:
            CommandObject ?

        Example:
            >>> tokenized_commands = ['echo', 'Hello     world', '>', './cmd/files/mop.md', '&&', 'echo', 'Hello', 'world']
        """

        main_command = tokenized_commands[0]

        if main_command in self.supported_commands:
            # PARSING AND CREATING COMMAND OBJECT ALGORITHM
            
            
            
            
            
            
            
            pass

        return 1