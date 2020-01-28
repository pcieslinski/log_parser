import argparse
from typing import List


stats_parser = argparse.ArgumentParser(
    prog='log-parser stats',
    description='Generates useful statistics and metrics based on the server log.'
)

stats_parser.add_argument('file',
                          type=str,
                          help='Path to the log file.')

stats_parser.add_argument('--since',
                          type=str,
                          help=('Date from which statistics will be calculated.'
                                ' Example: 01/Dec/2019:05:07:05')
                          )

stats_parser.add_argument('--until',
                          type=str,
                          help=('Date after which statistics will no longer be calculated.'
                                ' Example: 01/Dec/2019:05:07:05')
                          )

stats_parser.add_argument('--verbose',
                          '-v',
                          action='store_true',
                          help=argparse.SUPPRESS)


def stats_parse_args(args: List[str]) -> argparse.Namespace:
    return stats_parser.parse_args(args)
