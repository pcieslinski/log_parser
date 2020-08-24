from abc import ABC
from typing import NewType, List

from log_parser.parser.log_line import LogLine


class IStatistic(ABC):

    @staticmethod
    def calculate(data: List[LogLine]):
        pass


Statistic = NewType('Statistic', IStatistic)
