from argparse import Namespace

from log_parser.cli.main_args_parser import main_parse_args


def test_main_parse_args_return_correct_values_for_arguments():
    parsed_args = main_parse_args(['stats'])

    assert isinstance(parsed_args, Namespace)
    assert parsed_args.command == 'stats'
