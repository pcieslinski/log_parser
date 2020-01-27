from typing import Tuple
from argparse import Namespace
from collections import Counter

from log_parser.parser.parser import Parser
from log_parser.commands.icommand import ICommand
from log_parser.commands.stats import statistics as stat


class StatsCommand(ICommand):
    def __init__(self, parser: Parser) -> None:
        self.parser = parser

    def run(self, args: Namespace) -> Tuple[Counter, int, float]:
        data = list(self.parser.parse_log(args.file))

        n_requests = stat.NumberOfRequests.calculate(data)
        requests_per_seconds = stat.RequestsPerSecond.calculate(data)
        number_of_statuses = stat.NumberOfStatuses.calculate(data)

        return number_of_statuses, n_requests, requests_per_seconds
