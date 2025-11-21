from pydantic import BaseModel
from typing import Optional

class CommandObject(BaseModel):
    command: str
    args: list[str]
    stdin_redirect: Optional[str] = None
    stdout_redirect: Optional[str] = None
    operator: Optional[str] = None # "&&", "||", or None
    output: Optional[str] = None
    output_status_code: int = 0 # 0 succeeded 1 failed
    unsuported_command: bool = False

class CommandTreeNode:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left