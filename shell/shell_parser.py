from models import CommandObject
from typing import List

class ShellParser:
    """
    ShellParser is responsible for getting the tokenized commands and 
    parsing it to the CommandObjects data type
    representing the program flow.
    """

    def __init__(self, supported: set[str], redirects: set[str], operators: set[str]):
        self.supported_commands = supported
        self.operators = operators
        self.redirects = redirects

    def _create_command_object(self, token: str) -> None:
        """ Creates new CommandObject in the commands_flow_list

        Args:
            token (str): token from the command

        Return:
            None
        """
        self._commands_flow_list.append(CommandObject(command=token, args=[]))
        self.commands_flow_index+=1

    def _assign_redirect(self, redirect: str, redirect_file: str) -> None:
        """ Assigns redirect parameter to existing CommandObject

        Args:
            redirect (str): redirect token from command
            redirect_file (str): file which redirect will points to

        Return:
            None
        """
        redirect_command = self.redirects.get(redirect)
        setattr(self._commands_flow_list[self.commands_flow_index], redirect_command, redirect_file)

    def _assign_operator(self, operator: str) -> None:
        """ Assigns operator parameter to existing CommandObject
        
        Args:
            operator (str): operator token from the command

        Return:
            None
        """
        self._commands_flow_list[self.commands_flow_index].operator = operator

    def _assign_argument(self, argument: str) -> None:
        """ Assigns argument parameter to existing CommandObject list of args
        
        Args:
            argument (str): argument token from the command

        Return:
            None
        """
        self._commands_flow_list[self.commands_flow_index].args.append(argument)

    def _get_current_command_object(self) -> CommandObject:
        """ Returns current command object """
        return self._commands_flow_list[self.commands_flow_index]

    def parse(self, tokenized_commands: List[str]) -> List[CommandObject]:
        """Parses tokenized commands provided by user from the console.

        Args:
            list[str]: List of shell-compatible tokens.

        Returns:
            commands_flow_list 

        Example:
            >>> tokenized_commands = ['echo', 'Hello     world', '>', './cmd/files/mop.md', '&&', 'echo', 'Hello', 'world']
            @ Write the output example
            >>> Output
        """

        self._commands_flow_list = []
        self._commands_flow_index = -1
        
        for index, token in enumerate(tokenized_commands):
            if token in self.supported_commands:
                self._create_command_object(token)

            elif token in self.redirects:
                file_name = tokenized_commands[index + 1]
                self._assign_redirect(token, file_name)
    
            elif token in self.operators:
                self._assign_operator(token)

            else:
                current_command_object = self._get_current_command_object()

                if token == current_command_object.stdin_redirect or current_command_object.stdout_redirect:
                    continue

                self._assign_argument(token)

        return self._commands_flow_list