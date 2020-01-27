import datetime as dt

from log_parser.commands.stats.statistics import RequestsPerSecond


class TestRequestsPerSecond:

    def test_requests_per_second_calculates_correctly_statistic(self, data):
        assert RequestsPerSecond.calculate(data) == 2.0

    def test_extract_date_method_extracts_correctly_date_from_log_line(self, data):
        date = RequestsPerSecond.extract_date(data[0])

        assert isinstance(date, dt.datetime)
        assert date == dt.datetime(2019, 11, 30, 21, 3, 13)
