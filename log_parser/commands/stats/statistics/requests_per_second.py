from typing import List

from log_parser.services import date_service
from log_parser.parser.log_line import LogLine
from log_parser.commands.stats.statistics.istatistic import IStatistic


class RequestsPerSecond(IStatistic):

    @staticmethod
    def calculate(data: List[LogLine]) -> float:
        first_date = date_service.extract_date(log_line=data[0])
        last_date = date_service.extract_date(log_line=data[-1])

        seconds = (first_date - last_date).total_seconds()
        n_requests = len(data)

        try:
            return round(n_requests / seconds, 1)
        except ZeroDivisionError:
            return float(n_requests)
