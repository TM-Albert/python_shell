import os
import sys
import socket
from typing import Tuple

class ShellUtils:
    def __init__(self):
        pass
    
    
    def create_net_return_object(self, status_code: int, result: str):
        return (status_code, result)


    def net_getip(self, domain: str, s: socket.socket=None) -> Tuple[int, str]:
        """
        
        Returns:

        """
        try:
            
            ip = socket.gethostbyname(domain)
            return self.create_net_return_object(status_code=0, result=ip)
        
        except Exception as e:
            error_message = f"Class ShellUtils - Method net_getip - execution error: {e}"
            return self.create_net_return_object(status_code=1, result=error_message)


    def net_scanports(self):
        pass