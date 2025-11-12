import shlex

class ShellTokenizer:
    """
    ShellTokenizer is responsible for parsing and tokenizing shell-like commands.
    It uses Python's `shlex` to handle quoting, escaping, and POSIX-style syntax.
    """

    @staticmethod
    def describe_shlex_usage():
        """
        Explain how and why shlex is configured in this project.

        POSIX=True:
            Makes shlex follow standard Unix shell parsing rules (Bash, Dash, etc.).
            Handles quotes ('", escaping, and word splitting correctly.

        punctuation_chars=True:
            Treats characters such as |, &, <, >, and () as separate tokens.
            This is critical for distinguishing operators and redirects in command parsing.

        Example:
            Input:  echo "Hello   world" > out.txt && echo bye
            Tokens: ['echo', 'Hello   world', '>', 'out.txt', '&&', 'echo', 'bye']
        """
        print(ShellTokenizer.describe_shlex_usage.__doc__)

    @staticmethod
    def tokenize(user_input: str) -> list[str]:
        """Tokenize a user command into shell-style tokens.

        Uses Python's `shlex` library in POSIX mode to split input
        according to standard Unix shell parsing rules. Quoted strings,
        escaped spaces, and redirection or logical operators (e.g. `>`,
        `<`, `&&`, `||`) are preserved as individual tokens.

        Args:
            user_input (str): Raw command input from the user.

        Returns:
            list[str]: List of shell-compatible tokens.

        Example:
            >>> user_input = 'echo "Hello     world" > ./cmd/files/mop.md && echo Hello world'
            >>> tokenize(user_input)
            ['echo', 'Hello     world', '>', './cmd/files/mop.md', '&&', 'echo', 'Hello', 'world']
        """

        s = shlex.shlex(user_input, posix=True, punctuation_chars=True)
        tokens = list(s)

        return tokens