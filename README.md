# Python Shell Project

Python Shell Project simulates a minimal shell environment with built-in commands and support for external programs. It allows executing commands like `echo`, `pwd`, `cd`, and also provides custom network utilities.

---

## Features

- **Built-in Commands**: `echo`, `pwd`, `cd`, `exit`, `clear`, `mkdir`, `rmdir`, `touch`, `rm`, `net`.

- **Automatic Command Registration**: Any method starting with `cmd_` is automatically exposed as a shell command.

- **Network Utilities**:
  - `getip` – resolve a domain to its IP address.
  - `scanports` – scan TCP ports on a target host.

- **External Command Execution**: If a command is not built-in, attempts to run it via the system shell.

- **Portable**: Works on Windows, Linux, and macOS.

- **Command Result Contract**: All commands return a tuple:

  ```python
    (status_code: int, output_text: Optional[str], should_exit: bool)

    status_code: 0 = success, 1 = failure, 127 = command not found.
    output_text: The command output or error message.
    should_exit: Indicates if the shell should terminate (True only for exit).


## Installation

* Clone the repository:

```bash
git clone https://github.com/TM-Albert/shell_project.git
cd shell_project
```
* Make sure you have Python 3.8+


## Usage

```bash
from shell_executor import ShellExecutor

shell = ShellExecutor()
shell.run()
```


## Available Built-in Commands

| Command                         | Description                                                                     |
|-------------------------------- |-------------------------------------------------------------------------------- |
| `exit`                          | Exits the shell.                                                                |
| `echo`                          | Prints the provided arguments.                                                  |
| `pwd`                           | Displays the current working directory.                                         |
| `cd`                            | Changes the current working directory. Supports ~ for home and relative paths.  |
| `clear`                         | Clears the terminal screen.                                                     |
| `mkdir`                         | Creates a new directory.                                                        |
| `rmdir`                         | Removes an empty directory.                                                     |
| `touch`                         | Creates an empty file.                                                          |
| `rm`                            | Deletes a file.                                                                 |
| `net`                           | Network utility with subcommands: getip, scanports.                             |
| `type`                          | Shows if a command is built-in (to implement).                                  |
| `cat`                           | Display file content (to implement).                                            |

## Extending the Shell

* Adding a new built-in command is simple:
- Add a method to ShellBuiltins starting with cmd_.
- Ensure it returns a tuple: (status_code, output_text, should_exit).
- The command is automatically available without further registration.

* Example
```bash
def cmd_hello(self, _cmd, args):
    return (0, "Hello from Shell!", False)
```

## External Commands

* Commands not found in built-ins are automatically searched in the system PATH. They are executed via subprocess.run, capturing stdout and stderr. If the executable is not found, a command not found error is returned with status code 127.

## Network Commands

* The net command uses the ShellUtils module:
```text
net getip <domain>      # Resolves domain to IP address
net scanports <domain>  # Scans TCP ports on the target
```

## Author
* [Albert Grzegrzółka](https://github.com/TM-Albert)
