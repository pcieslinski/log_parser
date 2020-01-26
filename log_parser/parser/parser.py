from re import Pattern
from typing import Iterator, Union

from log_parser.parser.log_line import LogLine


class Parser:
    def __init__(self, pattern: Pattern) -> None:
        self.pattern = pattern

    def parse_log(self, file_path: str) -> Union[Iterator[LogLine], None]:
        with open(file_path, 'r') as f:
            try:
                next(f)  # skip header

                for line in f:
                    match = self.pattern.match(line)

                    if match:
                        yield LogLine(**match.groupdict())

            except StopIteration:
                return None
