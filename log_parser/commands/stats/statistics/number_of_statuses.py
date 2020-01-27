from typing import List
from collections import Counter

from log_parser.parser.log_line import LogLine
from log_parser.commands.stats.statistics.istatistic import IStatistic


class NumberOfStatuses(IStatistic):

    @staticmethod
    def calculate(data: List[LogLine]) -> Counter:
        statuses = [
            line.status for line in data
        ]

        result = Counter(statuses)

        return result
