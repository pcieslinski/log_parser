import argparse
from typing import List


main_parser = argparse.ArgumentParser(
    prog='log',
    description='A CLI tool for parsing logs.',
    usage=('log-parser <command> [<args>]\n'
           '\nlog-parser commands are:\n'
           'stats     Generates useful statistics and metrics based on the server log.\n')
)

main_parser.add_argument('command',
                         help='Subcommand to run')


def main_parse_args(args: List[str]) -> argparse.Namespace:
    return main_parser.parse_args(args)
