import os
import subprocess
from typing import Optional, Tuple

class ShellBuiltins:
    """
    Simulates built-in commands. Handlers now return a tuple:
    (status_code: int, output_text: Optional[str], should_exit: bool)

    status_code: 0 - executed successfully 
    status_code: 1 - executed unsuccessfully
    """

    def __init__(self):
        """
        Auto-register every builtin command.

        Rule (non-negotiable):
        A method is a builtin **iff** its name starts with ``cmd_``.
        The exposed command name is the part after the prefix.

        Examples
        --------
        cmd_echo  →  users type ``echo``
        cmd_ls    →  users type ``ls``

        Adding a new builtin is a single step:
        1. Add a method called cmd_<command_name> to this class.
        2. Nothing else.

        The one-liner below builds the lookup table once, at start-up,
        so the runtime cost is zero and the human cost is minimal.
        """
        self.builtin_commands = {
            name[4:]: getattr(self, name)
            for name in dir(self) if name.startswith('cmd_')
        }

        # Store the not-found handler as a separate, easily accessible attribute
        self.not_found_handler = self.cmd_not_found

        # --- DEFINED CONSTANTS FOR RETURN VALUES ---
        self.STATUS_CODE_SUCCESS: int = 0
        self.STATUS_CODE_FAILED: int = 1
        self.SHOULD_EXIT: bool = True
        self.SHOULD_NOT_EXIT: bool = False
        self.COMMAND_NOT_FOUND_EXIT_FLAG: int = 127
        # -------------------------------------------

    def _find_executable_in_path(self, executable_file_name: str) -> Optional[str]:
        """
        Searches directories listed in the PATH environment variable for an executable file.
        """
        # Get PATH environment variable and split it by ':'
        path_dirs = os.environ.get("PATH", "").split(os.pathsep) 
        
        for folder_path in path_dirs:
            potential_path = os.path.join(folder_path, executable_file_name)
            
            # Check if the path exists, is a file, and is executable
            if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
                return potential_path
        
        return None

    def cmd_exit(self, *_) -> Tuple[int, Optional[str], bool]:
        """Exits the program"""
        print("Exiting shell.")
        return (self.STATUS_CODE_SUCCESS, None, self.SHOULD_EXIT)

    def cmd_echo(self, _cmd, args) -> Tuple[int, Optional[str], bool]:
        """Echo back user arguments."""
        output = " ".join(args)
        return (self.STATUS_CODE_SUCCESS, output, self.SHOULD_NOT_EXIT)

    def cmd_type(self) -> Tuple[int, Optional[str], bool]:
        """Show if a command is builtin."""
        pass

    def cmd_pwd(self) -> Tuple[int, Optional[str], bool]:
        """Displays current working directory."""
        output = os.getcwd()
        return (self.STATUS_CODE_SUCCESS, output, self.SHOULD_NOT_EXIT)

    def cmd_cd(self) -> Tuple[int, Optional[str], bool]:
        """
        
        """
        pass

    def cmd_cat(self, cmd, args) -> Tuple[int, Optional[str], bool]:
        """
        
        """
        pass

    def cmd_not_found(self, cmd_name: str, args: list[str]) -> Tuple[int, Optional[str], bool]:
        """
        Handler for unknown commands. Attempts to find and execute the command as
        an external program via subprocess.
        """

        executable_path = self._find_executable_in_path(cmd_name)

        if executable_path is None:
            # Command not found, return status 127
            error_output = f"{cmd_name}: command not found"
            return self.COMMAND_NOT_FOUND_EXIT_FLAG, error_output, self.SHOULD_NOT_EXIT 
        
        # Command found, execute it
        try:
            # subprocess.run executes the command.
            # capture_output=True captures stdout and stderr.
            # text=True decodes stdout/stderr as text.

            result = subprocess.run(
                [executable_path, *args], 
                capture_output=True, 
                text=True,
                check=False # Do not raise CalledProcessError for non-zero exit codes
            )

            # Combine stdout and stderr for the output buffer
            output = (result.stdout + result.stderr).strip()

            # Return the external command's return code and use constant for exit flag
            return result.returncode, output, self.SHOULD_NOT_EXIT
        
        except Exception as e:
            # Catch execution errors (e.g., permission denied)
            error_output = f"shell: execution error for {cmd_name}: {e}"
            # Use constant for failure code and exit flag
            return self.STATUS_CODE_FAILED, error_output, self.SHOULD_NOT_EXIT
        


if __name__ == "__main__":
    c = ShellBuiltins()
    print(c.builtin_commands)