from typing import Callable
from argparse import Namespace
from datetime import datetime as dt

from log_parser.services import date_service
from log_parser.parser.parser import Parser
from log_parser.parser.log_line import LogLine
from log_parser.renderers import StatsOutputRenderer
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

    def run(self, args: Namespace) -> None:
        data = list(self.parser.parse_log(args.file))

        if args.since:
            since_filter = self.filter_since(args.since)
            data = list(filter(since_filter, data))

        if args.until:
            until_filter = self.filter_until(args.until)
            data = list(filter(until_filter, data))

        n_requests = stat.NumberOfRequests.calculate(data)
        responses_statuses_count = stat.NumberOfStatuses.calculate(data)
        requests_per_second = stat.RequestsPerSecond.calculate(data)
        avg_size_for_2xx = stat.AverageResponseSize.calculate(data)

        StatsOutputRenderer(
            n_requests=n_requests,
            responses_statuses_count=responses_statuses_count,
            requests_per_second=requests_per_second,
            avg_size_for_2xx=avg_size_for_2xx
        ).render()
