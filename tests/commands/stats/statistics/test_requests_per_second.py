from log_parser.commands.stats.statistics import RequestsPerSecond


class TestRequestsPerSecond:

    def test_requests_per_second_calculates_correctly_statistic(self, data):
        assert RequestsPerSecond.calculate(data) == 0.2
