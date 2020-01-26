import pytest
from mock import Mock
from typing import List, Tuple
from collections import Counter
from dataclasses import dataclass

from log_parser.commands import StatsCommand
from log_parser.parser.log_line import LogLine


@pytest.fixture
def data(log_line_data) -> List[LogLine]:
    return [
        LogLine(**log_line_data),
        LogLine(**log_line_data)
    ]


@pytest.fixture
def mock_parser_with_data(data: List[LogLine]) -> Tuple[Mock, List[LogLine]]:
    parser = Mock()
    parser.parse_log.return_value = data
    return parser, data


@pytest.fixture
def stub_args() -> dataclass:
    @dataclass
    class StubArgs:
        file: str

    return StubArgs(file='./test.log2')


class TestStatsCommand:

    def test_stats_command_initialize_correctly(self, mock_parser_with_data):
        mock_parser, _ = mock_parser_with_data
        command = StatsCommand(parser=mock_parser)

        assert isinstance(command, StatsCommand)
        assert hasattr(command, 'parser')
        assert command.parser is mock_parser

    def test_stats_command_runs_correctly(self, mock_parser_with_data, stub_args):
        mock_parser, data = mock_parser_with_data

        command = StatsCommand(parser=mock_parser)
        statuses_counts, n_requests = command.run(args=stub_args)

        mock_parser.parse_log.assert_called_once_with('./test.log2')
        assert isinstance(statuses_counts, Counter)
        assert statuses_counts['test_status'] == 2
        assert n_requests == 2
