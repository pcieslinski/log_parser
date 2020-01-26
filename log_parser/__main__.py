import sys
from typing import Union

from log_parser.cli import parse_args
from log_parser.parser import parser
from log_parser.commands import StatsCommand


def main() -> None:
    args = parse_args(sys.argv[1:])

    command = StatsCommand(parser=parser)
    statuses_counts, n_requests = command.run(args=args)

    print(f'Number of requests: {n_requests}')
    print(f'Responses statuses count:')
    for status, count in statuses_counts.items():
        print(f'{status}: {count}')


def runner() -> Union[None, str]:
    try:
        main()
    except Exception as exc:
        return f'{exc.__class__.__name__}: {exc}'


if __name__ == '__main__':
    runner()
