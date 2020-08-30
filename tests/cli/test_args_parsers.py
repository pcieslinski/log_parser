from argparse import Namespace

import pytest

from log_parser.cli.args_parsers import main_parse_args, stats_parse_args


def test_main_parse_args_return_correct_values_for_arguments():
    parsed_args = main_parse_args(['stats'])

    assert isinstance(parsed_args, Namespace)
    assert parsed_args.command == 'stats'


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
def test_stats_parse_args_return_correct_values_for_arguments(args, file, since, until):
    parsed_args = stats_parse_args(args)

    assert isinstance(parsed_args, Namespace)
    assert parsed_args.file == file
    assert parsed_args.since == since
    assert parsed_args.until == until
