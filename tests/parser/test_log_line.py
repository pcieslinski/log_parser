from log_parser.parser.log_line import LogLine


class TestLogLine:

    def test_log_line_initialize_correctly(self, log_line_data):
        log_line = LogLine(**log_line_data)

        assert log_line.prefix == 'test_prefix'
        assert log_line.host == 'test_host'
        assert log_line.identity == 'test_identity'
        assert log_line.user == 'test_user'
        assert log_line.date == 'test_date'
        assert log_line.request == 'test_request'
        assert log_line.status == 'test_status'
        assert log_line.bytes == 'test_bytes'
        assert log_line.referer == 'test_referer'
        assert log_line.user_agent == 'test_user_agent'
