import os
import sys
from executor import ShellExecutor
from models import CommandObject
from typing import List

class ShellParser:
    """
    ShellParser is responsible for getting the tokenized commands and 
    parsing it to the CommandObjects data type
    representing the program flow.
    """

    def __init__(self):
        self.supported_commands = ShellExecutor().supported_commands
        self.operators = ShellExecutor().operators
        self.redirects = ShellExecutor().redirects

        self.commands_flow_list: List[CommandObject] = []
        self.commands_flow_index: int = 0

    def create_command_object(self, token: str) -> None:
        """ Creates new CommandObject in the commands_flow_list

        Args:
            token (str): token from the command

        Return:
            None
        """
        self.commands_flow_list.append(CommandObject(command=token, args=[]))
        self.commands_flow_index+=1

    def assign_redirect(self, redirect: str, redirect_file: str) -> None:
        """ Assigns redirect parameter to existing CommandObject

        Args:
            redirect (str): redirect token from command
            redirect_file (str): file which redirect will points to

        Return:
            None
        """
        redirect_command = self.redirects.get(redirect)
        setattr(self.commands_flow_list[self.commands_flow_index], redirect_command, redirect_file)

    def assign_operator(self, operator: str) -> None:
        """ Assigns operator parameter to existing CommandObject
        
        Args:
            operator (str): operator token from the command

        Return:
            None
        """
        self.commands_flow_list[self.commands_flow_index].operator = operator

    def assign_argument(self, argument: str) -> None:
        """ Assigns argument parameter to existing CommandObject list of args
        
        Args:
            argument (str): argument token from the command

        Return:
            None
        """
        self.commands_flow_list[self.commands_flow_index].args.append(argument)

    def parse(self, tokenized_commands: List[str]) -> List[CommandObject]:
        """Parses tokenized commands provided by user from the console.

        Args:
            list[str]: List of shell-compatible tokens.

        Returns:
            commands_flow_list 

        Example:
            >>> tokenized_commands = ['echo', 'Hello     world', '>', './cmd/files/mop.md', '&&', 'echo', 'Hello', 'world']
            >>> Output
        """
        
        for index, token in enumerate(tokenized_commands):
            if token in self.supported_commands:
                self.create_command_object(token)

            elif token in self.redirects:
                file_name = tokenized_commands[index + 1]
                self.assign_redirect(token, file_name)
    
            elif token in self.operators:
                self.assign_operator(token)

            else:
                self.assign_argument(token)

        return self.commands_flow_list