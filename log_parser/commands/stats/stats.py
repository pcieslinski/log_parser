from argparse import Namespace
from collections import Counter
from typing import Callable, Tuple
from datetime import datetime as dt

from log_parser.services import date_service
from log_parser.parser.parser import Parser
from log_parser.parser.log_line import LogLine
from log_parser.commands.icommand import ICommand
from log_parser.commands.stats import statistics as stat


SinceFilter = Callable[[LogLine], bool]
UntilFilter = Callable[[LogLine], bool]


class StatsCommand(ICommand):
    def __init__(self, parser: Parser) -> None:
        self.parser = parser

    @staticmethod
    def filter_since(since: str) -> SinceFilter:
        since_date = dt.strptime(since, date_service.format)

        def is_older(log_line: LogLine) -> bool:
            log_line_date = date_service.extract_date(log_line)
            return True if log_line_date > since_date else False

        return is_older

    @staticmethod
    def filter_until(until: str) -> UntilFilter:
        until_date = dt.strptime(until, date_service.format)

        def is_earlier(log_line: LogLine) -> bool:
            log_line_date = date_service.extract_date(log_line)
            return True if log_line_date < until_date else False

        return is_earlier

    def run(self, args: Namespace) -> Tuple[Counter, int, float, str]:
        data = list(self.parser.parse_log(args.file))

        if args.since:
            since_filter = self.filter_since(args.since)
            data = list(filter(since_filter, data))

        if args.until:
            until_filter = self.filter_until(args.until)
            data = list(filter(until_filter, data))

        n_requests = stat.NumberOfRequests.calculate(data)
        requests_per_seconds = stat.RequestsPerSecond.calculate(data)
        number_of_statuses = stat.NumberOfStatuses.calculate(data)
        avg_size_for_2xx = stat.AverageResponseSize.calculate(data)

        return number_of_statuses, n_requests, requests_per_seconds, avg_size_for_2xx
