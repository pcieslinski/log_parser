import pytest
from mock import Mock, patch
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

    @patch('log_parser.commands.stats.statistics.NumberOfRequests.calculate')
    @patch('log_parser.commands.stats.statistics.RequestsPerSecond.calculate')
    @patch('log_parser.commands.stats.statistics.NumberOfStatuses.calculate')
    def test_stats_command_runs_correctly(self, mock_n_statuses, mock_requests_per_second,
                                          mock_n_requests, mock_parser_with_data, stub_args):
        mock_n_statuses.return_value = Counter(['200', '200'])
        mock_requests_per_second.return_value = 2.0
        mock_n_requests.return_value = 2

        mock_parser, data = mock_parser_with_data

        command = StatsCommand(parser=mock_parser)
        number_of_statuses, n_requests, requests_per_seconds = command.run(args=stub_args)

        mock_parser.parse_log.assert_called_once_with('./test.log2')
        assert isinstance(number_of_statuses, Counter)
        assert number_of_statuses['200'] == 2
        assert n_requests == 2
        assert requests_per_seconds == 2.0
