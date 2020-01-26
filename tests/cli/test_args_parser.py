import pytest
from argparse import Namespace

from log_parser.cli import parse_args


@pytest.mark.parametrize('args,file,since,until', [
    (
            ['./test.log2'],
            './test.log2',
            None,
            None),
    (
            ['./test.log2', '--since', '2020-01-01'],
            './test.log2',
            '2020-01-01',
            None),
    (
           ['./test.log2', '--since', '2020-01-01', '--until', '2020-01-25'],
           './test.log2',
           '2020-01-01',
           '2020-01-25'
    )
])
def test_parse_args_return_correct_values_for_arguments(args, file, since, until):
    parsed_args = parse_args(args)

    assert isinstance(parsed_args, Namespace)
    assert parsed_args.file == file
    assert parsed_args.since == since
    assert parsed_args.until == until
