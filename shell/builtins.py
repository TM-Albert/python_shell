import os
import sys
import subprocess

class shellBuiltins:
    def __init__(self):
        pass

    def cmd_exit(self, *_):
        """Exits the program"""
        return True

    def cmd_echo(self):
        """
        
        """
        pass

    def cmd_type(self):
        """
        
        """
        pass

    def cmd_pwd(self):
        """Displays current working directory."""
        print(os.getcwd())

    def cmd_cd(self):
        """
        
        """
        pass

    def cmd_cat(self):
        """
        
        """
        pass

    def cmd_not_found(self):
        """
        
        """
        pass