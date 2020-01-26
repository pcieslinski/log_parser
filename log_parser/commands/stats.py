from typing import Tuple
from argparse import Namespace
from collections import Counter

from log_parser.parser.parser import Parser


class StatsCommand:
    def __init__(self, parser: Parser) -> None:
        self.parser = parser

    def run(self, args: Namespace) -> Tuple[Counter, int]:
        print(f'Processing file {args.file} with args: {args}')

        data = self.parser.parse_log(args.file)

        statuses = [
            line.status for line in data
        ]

        statuses_counts = Counter(statuses)

        return statuses_counts, len(statuses)
