from typing import Any


class LogParserException(Exception):
    def __init__(self, message: str, details: Any = None, type: str = 'Error'):
        self.message = message
        self.details = details or message
        self.type = type

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message
