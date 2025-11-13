from pydantic import BaseModel
from collections import deque

class CommandObject(BaseModel):
    command: str
    args: list[str]
    stdin_redirect: str | None = None
    stdout_redirect: str | None = None
    operator: str | None = None # "&&", "||", or None

class CommandsTree:
    def __init__(self):
        pass

    

class CommandTreeNode:
    def __init__(self, data):
        self.data = data
        
