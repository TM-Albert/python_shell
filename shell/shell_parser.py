from shell_models import CommandObject
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
        """ Creates new CommandObject in the commands_flow_list """
        self._commands_flow_list.append(CommandObject(command=token, args=[]))
        self._commands_flow_index+=1

    def _assign_redirect(self, redirect: str, redirect_file: str) -> None:
        """ Assigns redirect parameter to existing CommandObject

        Args:
            redirect (str): redirect token from command
            redirect_file (str): file which redirect will points to

        Return:
            None
        """
        redirect_command = self.redirects.get(redirect)
        setattr(self._get_current_command_object(), redirect_command, redirect_file)

    def _assign_operator(self, operator: str) -> None:
        """ Assigns operator parameter to existing CommandObject """
        self._get_current_command_object().operator = operator

    def _assign_argument(self, argument: str) -> None:
        """ Assigns argument parameter to existing CommandObject list of args """
        self._get_current_command_object().args.append(argument)

    def _get_current_command_object(self) -> CommandObject:
        """ Returns current command object """
        return self._commands_flow_list[self._commands_flow_index]
    
    def _token_assigned_to_stdin(self, token: str) -> bool:
        """Check if token is assign to stdin or stdout parameter in CommandObject"""

        current_command_object = self._get_current_command_object()

        if token == current_command_object.stdin_redirect or current_command_object.stdout_redirect:
            return True
        
        return False
    
    def _lookup_command(self, command: str) -> bool:
        """Check if command is in list of supported commands"""

        if command in self.supported_commands:
            return True
        
        return False
    
    def _create_unsuported_command_object(self, command: str):
        """Creates unsuported command object"""
        self._commands_flow_list.append(CommandObject(command=command, args=[], unsuported_command=True))

    def parse(self, tokenized_commands: List[str]) -> List[CommandObject]:
        """Parses tokenized commands provided by user from the console.

        Args:
            list[str]: List of shell-compatible tokens.

        Returns:
            commands_flow_list 

        Example:
            >>> tokenized_commands = ['echo', 'Hello     world', '>', './cmd/files/mop.md', '&&', 'echo', 'Hello', 'world']
            >>> commands_flow_list =
            >>> [
            >>>        CommandObject(
            >>>            command='echo', 
            >>>            args=['Hello     world'], 
            >>>            stdin_redirect=None, 
            >>>            stdout_redirect='./cmd/files/mop.md', 
            >>>            operator='&&', 
            >>>            output=None, 
            >>>            output_status_code=0
            >>>        ), 
            >>>        CommandObject(
            >>>            command='echo', 
            >>>            args=['Hello world'], 
            >>>            stdin_redirect=None, 
            >>>            stdout_redirect=None, 
            >>>            operator=None, 
            >>>            output=None, 
            >>>            output_status_code=0
            >>>        )
            >>>  ]
        """

        self._commands_flow_list = []
        self._commands_flow_index = -1

        main_command = tokenized_commands[0]
        command_supported = self._lookup_command(main_command)

        if command_supported:
            for index, token in enumerate(tokenized_commands):

                if token in self.supported_commands:
                    self._create_command_object(token)

                elif token in self.redirects:
                    file_name = tokenized_commands[index + 1]
                    self._assign_redirect(token, file_name)
        
                elif token in self.operators:
                    self._assign_operator(token)

                else:
                    if self._token_assigned_to_stdin(token):
                        continue

                    self._assign_argument(token)
        else:
            self._create_unsuported_command_object(main_command)
        
        return self._commands_flow_list