from log_parser.commands.stats.statistics import NumberOfRequests


def test_number_of_requests_calculates_correctly_statistic(data):
    assert NumberOfRequests.calculate(data) == 2
