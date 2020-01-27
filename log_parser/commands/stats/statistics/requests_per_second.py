import datetime as dt
from typing import List

from log_parser.parser.log_line import LogLine
from log_parser.commands.stats.statistics.istatistic import IStatistic


DATE_FORMAT = '%d/%b/%Y:%H:%M:%S'
DATE_BASE_INDEX = 0
DATE_UTC_INDEX = 1


class RequestsPerSecond(IStatistic):

    @staticmethod
    def extract_date(log_line: LogLine) -> dt.datetime:
        date = log_line.date.split(' ')[DATE_BASE_INDEX]
        return dt.datetime.strptime(date, DATE_FORMAT)

    @staticmethod
    def calculate(data: List[LogLine]) -> float:
        first_date = RequestsPerSecond.extract_date(data[0])
        last_date = RequestsPerSecond.extract_date(data[-1])

        seconds = (first_date - last_date).total_seconds()
        n_requests = len(data)

        try:
            return round(n_requests / seconds, 1)
        except ZeroDivisionError:
            return float(n_requests)
