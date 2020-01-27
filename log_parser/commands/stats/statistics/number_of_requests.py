from typing import List

from log_parser.parser.log_line import LogLine
from log_parser.commands.stats.statistics.istatistic import IStatistic


class NumberOfRequests(IStatistic):

    @staticmethod
    def calculate(data: List[LogLine]) -> int:
        return len(data)
