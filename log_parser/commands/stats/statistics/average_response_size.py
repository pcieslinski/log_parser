import math
from typing import List

from log_parser.parser.log_line import LogLine
from log_parser.commands.stats.statistics.istatistic import IStatistic


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
