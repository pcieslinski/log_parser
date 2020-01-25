import sys
from typing import Union

from log_parser.cli import parse_args
from log_parser.request_counter import RequestCounter


def main() -> None:
    args = parse_args(sys.argv[1:])

    counter = RequestCounter(args.file)
    n_requests = counter.count_requests()

    print(f'Number of requests: {n_requests}')


def runner() -> Union[None, str]:
    try:
        main()
    except Exception as exc:
        return f'{exc.__class__.__name__}: {exc}'


if __name__ == '__main__':
    runner()
