import pytest

from log_parser.exceptions import LogParserException


@pytest.fixture
def log_parser_exception():
    return LogParserException(
        message='test_message',
        details='test_details',
        type='test_type'
    )


class TestLogParserException:

    @pytest.mark.parametrize('kwargs,message,details,type', [
        (dict(
            message='test_message',
            details='test_details',
            type='test_type'
        ), 'test_message', 'test_details', 'test_type'),
        (dict(
            message='test_message',
            type='test_type'
        ), 'test_message', 'test_message', 'test_type'),
        (dict(
            message='test_message',
        ), 'test_message', 'test_message', 'Error')
    ])
    def test_log_parser_exception_initialize_correctly(self, kwargs, message, details, type):
        exc = LogParserException(**kwargs)

        assert isinstance(exc, LogParserException)
        assert exc.message == message
        assert exc.details == details
        assert exc.type == type

    def test__str__method_returns_message_attribute(self, log_parser_exception):
        assert str(log_parser_exception) == 'test_message'

    def test__repr__method_returns_message_attribute(self, log_parser_exception):
        assert repr(log_parser_exception) == 'test_message'
