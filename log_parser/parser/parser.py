import os
from re import Pattern
from typing import Iterator, Union

from log_parser.parser.log_line import LogLine
from log_parser.exceptions import LogParserException


class Parser:
    def __init__(self, pattern: Pattern) -> None:
        self.pattern = pattern

    def parse_log(self, file_path: str) -> Union[Iterator[LogLine], None]:

        if not os.path.isfile(file_path):
            raise LogParserException(
                message=f'The file: {file_path} does not exist.',
                type='FileNotFoundError'
            )

        with open(file_path, 'r') as f:
            try:
                for line in f:
                    match = self.pattern.match(line)

                    if match:
                        yield LogLine(**match.groupdict())

            except StopIteration:
                return None
