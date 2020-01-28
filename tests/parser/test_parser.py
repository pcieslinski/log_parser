import pytest
from mock import Mock, mock_open, patch
from typing import Tuple

from log_parser.parser.parser import Parser
from log_parser.parser.log_line import LogLine


@pytest.fixture
def mock_pattern() -> Mock:
    return Mock()


@pytest.fixture
def parser_with_mock_pattern(mock_pattern: Mock) -> Tuple[Parser, Mock]:
    return Parser(pattern=mock_pattern), mock_pattern


@pytest.fixture
def read_data() -> str:
    return 'REQUEST_DATA'


class TestParser:

    def test_parser_initialize_correctly(self, parser_with_mock_pattern):
        parser, mock_pattern = parser_with_mock_pattern

        assert isinstance(parser, Parser)
        assert hasattr(parser, 'pattern')
        assert parser.pattern is mock_pattern

    def test_parse_log_returns_generator_of_log_lines(self,
                                                      parser_with_mock_pattern,
                                                      log_line_data,
                                                      read_data):
        parser, mock_pattern = parser_with_mock_pattern
        mock_pattern.match.return_value.groupdict.return_value = log_line_data[0]

        m = mock_open(read_data=read_data)

        with patch('builtins.open', m, create=True):
            generator = parser.parse_log(file_path='./test.log2')
            result = next(generator)

            m.assert_called_once_with('./test.log2', 'r')
            mock_pattern.match.assert_called_once_with('REQUEST_DATA')
            assert result == LogLine(**log_line_data[0])

    def test_parse_log_returns_none_when_called_on_empty_file(self,
                                                              parser_with_mock_pattern):
        parser, mock_pattern = parser_with_mock_pattern

        m = mock_open(read_data='')

        with patch('builtins.open', m, create=True):
            generator = parser.parse_log('./test.log2')
            result = list(generator)

            m.assert_called_once_with('./test.log2', 'r')
            assert mock_pattern.match.call_count == 0
            assert result == []

    def test_parse_log_raises_exception_when_called_with_not_existing_file(self,
                                                                           parser_with_mock_pattern):
        parser, _ = parser_with_mock_pattern
        with pytest.raises(FileNotFoundError):
            generator = parser.parse_log(file_path='./test.log2')
            result = list(generator)
