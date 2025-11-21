import os
import sys
from typing import Optional
from shell_models import CommandObject
from shell_tokenizer import ShellTokenizer 
from shell_parser import ShellParser
from shell_builtins import ShellBuiltins

class ShellExecutor:
    """
    ShellExecutor is responsible for executing the shell program
    """

    def __init__(self):
        builtins = ShellBuiltins()
        self.builtin_commands = builtins.builtin_commands
        self.cmd_not_found_handler = builtins.not_found_handler

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

    def list_supported_commands(self):
        """ Returns a list of currently supported shell commands. """
        print("Supported Builtin Commands:")
        for i, cmd in enumerate(self.supported_commands.keys(), 1):
            print(f"{i}- {cmd.upper()}")

    def execute(self, command_list: list[CommandObject]):
        """ 
        Execution of the command object with support for status codes, 
        redirection, and command chaining (&&, ||).
        """

        should_exist: bool = False
        prev_status: bool = 0 # Initial status is success (0)

        for i, command_object in enumerate(command_list):
            cmd: str = command_object.command
            args: list[str] = command_object.args

            # --- 1. COMMAND CHAINING LOGIC ---
            
            # If this is not the first command, check the operator of the previous command 
            # (assuming the operator is set on the command object it precedes)

            if i > 0:
                prev_command = command_list[i-1]
                op = prev_command.operator

                # Skip if previous command failed AND operator was '&&' (Success dependency)
                if op == "&&" and prev_status != 0:
                    print(f"Skipping '{cmd}' due to failed preceding command.")
                    prev_status = 0 # Shell behavior: clear status after skipping
                    continue
                
                # Skip if previous command succeeded AND operator was '||' (Failure dependency)
                if op == "||" and prev_status == 0:
                    print(f"Skipping '{cmd}' due to successful preceding command.")
                    prev_status = 0 # Shell behavior: clear status after skipping
                    continue
                
                # If operator is None or ';', we always execute.

            # --- 2. SELECT HANDLER AND EXECUTE ---
            
            status_code: int
            output_text: Optional[str]
            
            if command_object.unsuported_command:
                # Execute the 'command not found' handler which now runs external commands
                status_code, output_text, should_exit = self.cmd_not_found_handler(cmd, args)
            else:
                # Execute the built-in handler
                handler = self.builtin_commands.get(cmd)
                if handler:
                    status_code, output_text, should_exit = handler(cmd, args)
                else:
                    # Should not happen with correct parsing
                    sys.stderr.write(f"Internal Error: Handler for '{cmd}' not found.\n")
                    status_code, output_text, should_exit = 1, None, False
            
            # Update the status and output on the command object
            command_object.output_status_code = status_code
            command_object.output = output_text
            
            # Set status for the next command's chaining check
            prev_status = status_code

            # --- 3. REDIRECTION AND STANDARD OUTPUT HANDLING ---

            if output_text is not None and output_text.strip():
                if command_object.stdout_redirect:
                    # Handle STDOUT Redirection (>)
                    try:
                        # Use 'w' to overwrite, similar to standard shell behavior
                        with open(command_object.stdout_redirect, 'w') as f:
                            f.write(output_text + "\n")
                    except IOError as e:
                        # Log redirection failure, set status code
                        sys.stderr.write(f"shell: cannot redirect output to {command_object.stdout_redirect}: {e}\n")
                        prev_status = 1 # Redirection failure sets status code to 1
                else:
                    # If no redirection, print to standard output
                    print(output_text)
            
            # --- 4. EXIT CHECK ---
            if should_exit:
                return should_exit
        
        return should_exit


    def run(self):
        """ Main shell loop """

        while True:
            # Output buffer
            sys.stdout.write("$ ")
            sys.stdout.flush() # forces Python to empty the buffer immediately and write it to the terminal.
            line = sys.stdin.readline()

            if not line.strip():
                continue

            tokenized_line = ShellTokenizer().tokenize(line)

            parser = ShellParser(
                supported=self.builtin_commands,
                operators=self.operators,
                redirects=self.redirects
            )

            command_flow = parser.parse(tokenized_line)

            should_exit = self.execute(command_flow)

            if should_exit:
                break

if __name__ == "__main__":
    se = ShellExecutor()
    se.run()