import math
from typing import List
from collections import Counter

from log_parser.services import date_service
from log_parser.parser.log_line import LogLine
from log_parser.commands.stats.istatistic import IStatistic


SIZES_NAMES = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')


class AverageResponseSize(IStatistic):

    @staticmethod
    def convert_size(size_bytes: float) -> str:
        if size_bytes == 0:
            return '0B'

        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)

        return "%s%s" % (s, SIZES_NAMES[i])

    @staticmethod
    def calculate(data: List[LogLine]) -> str:
        bytes_for_2xx = [
            int(line.bytes) for line in data
            if line.status.startswith('2')
        ]

        n_requests = len(bytes_for_2xx)
        n_bytes = sum(bytes_for_2xx)

        return AverageResponseSize.convert_size(n_bytes / n_requests)


class NumberOfStatuses(IStatistic):

    @staticmethod
    def calculate(data: List[LogLine]) -> Counter:
        statuses = [
            line.status for line in data
        ]

        result = Counter(statuses)

        return result


class NumberOfRequests(IStatistic):

    @staticmethod
    def calculate(data: List[LogLine]) -> int:
        return len(data)


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
