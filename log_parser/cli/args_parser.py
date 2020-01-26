import argparse
from typing import List


parser = argparse.ArgumentParser(
    prog='log-parser',
    description='A CLI tool for parsing logs.'
                ' Generates useful statistics and metrics based on the server log.'
)

parser.add_argument('file',
                    type=str,
                    help='Path to the log file.')

parser.add_argument('--since',
                    type=str,
                    help='The date that marks the start of statistics generation.')

parser.add_argument('--until',
                    type=str,
                    help='The date that marks the end of statistics generation.')


def parse_args(args: List[str]) -> argparse.Namespace:
    return parser.parse_args(args)
