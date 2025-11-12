from pydantic import BaseModel

class CommandObject(BaseModel):
    command: str
    args: list[str]
    stdin_redirect: str | None = None
    stdout_redirect: str | None = None
    operator: str | None = None # "&&", "||", or None