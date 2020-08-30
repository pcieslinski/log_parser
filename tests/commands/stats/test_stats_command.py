import pytest
from mock import Mock, patch
from typing import List, Tuple
from dataclasses import dataclass

from log_parser.commands import StatsCommand
from log_parser.parser.log_line import LogLine


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
        since: str = None
        until: str = None

    return StubArgs


class TestStatsCommand:

    def test_stats_command_initialize_correctly(self, mock_parser_with_data):
        mock_parser, _ = mock_parser_with_data
        command = StatsCommand(parser=mock_parser)

        assert isinstance(command, StatsCommand)
        assert hasattr(command, 'parser')
        assert command.parser is mock_parser

    def test_filter_since_works_correctly(self, data):
        since_filter = StatsCommand.filter_since(since='30/Nov/2019:21:03:05')

        result = list(filter(since_filter, data))

        assert len(result) == 1
        assert result[0].date == '30/Nov/2019:21:03:13 +0100'

    def test_filter_until_works_correctly(self, data):
        until_filter = StatsCommand.filter_until(until='30/Nov/2019:21:03:05')

        result = list(filter(until_filter, data))

        assert len(result) == 1
        assert result[0].date == '30/Nov/2019:21:03:00 +0100'

    @patch('log_parser.commands.stats.statistics.NumberOfRequests.calculate')
    @patch('log_parser.commands.stats.statistics.RequestsPerSecond.calculate')
    @patch('log_parser.commands.stats.statistics.NumberOfStatuses.calculate')
    @patch('log_parser.commands.stats.statistics.AverageResponseSize.calculate')
    def test_stats_command_runs_correctly(
            self, mock_avg_size, mock_n_statuses, mock_requests_per_second,
            mock_n_requests, mock_parser_with_data, stub_args
    ):
        stub_args = stub_args(file='./test.log2')

        mock_parser, data = mock_parser_with_data

        command = StatsCommand(parser=mock_parser)
        command.run(args=stub_args)

        mock_parser.parse_log.assert_called_once_with('./test.log2')
        mock_n_statuses.assert_called_once_with(data)
        mock_requests_per_second.assert_called_once_with(data)
        mock_n_requests.assert_called_once_with(data)
        mock_avg_size.assert_called_once_with(data)
