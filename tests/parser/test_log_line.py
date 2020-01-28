from log_parser.parser.log_line import LogLine


class TestLogLine:

    def test_log_line_initialize_correctly(self, log_line_data):
        log_line = LogLine(**log_line_data[0])

        assert log_line.prefix == 'Nov 30 21:03:13 actify3-test-vm1 gunicorn[53253]'
        assert log_line.host == '172.16.3.14'
        assert log_line.identity == '-'
        assert log_line.user == '-'
        assert log_line.date == '30/Nov/2019:21:03:13 +0100'
        assert log_line.request == 'GET /internal/user/c1df9cd0-/agenda/2019-11-30/2019-12-01 HTTP/1.1'
        assert log_line.status == '200'
        assert log_line.bytes == '720'
        assert log_line.referer == '-'
        assert log_line.user_agent == 'python-requests/2.22.0'
