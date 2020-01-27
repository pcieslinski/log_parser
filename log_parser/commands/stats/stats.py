from typing import Tuple
from argparse import Namespace
from collections import Counter
from datetime import datetime as dt

from log_parser.parser.parser import Parser


class StatsCommand:
    def __init__(self, parser: Parser) -> None:
        self.parser = parser

    def run(self, args: Namespace) -> Tuple[Counter, int, float]:
        print(f'Processing file {args.file} with args: {args}')

        data = self.parser.parse_log(args.file)
        data = list(data)

        statuses = [
            line.status for line in data
        ]

        statuses_counts = Counter(statuses)

        first = data[0].date.split(' ')[0]
        first = dt.strptime(first, '%d/%b/%Y:%H:%M:%S')
        last = data[-1].date.split(' ')[0]
        last = dt.strptime(last, '%d/%b/%Y:%H:%M:%S')

        seconds = (first - last).total_seconds()
        n_requests = len(statuses)

        requests_per_seconds = n_requests / seconds

        return statuses_counts, len(statuses), requests_per_seconds
