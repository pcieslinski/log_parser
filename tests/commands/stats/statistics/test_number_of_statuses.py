from collections import Counter

from log_parser.commands.stats.statistics import NumberOfStatuses


def test_number_of_statuses_calculates_correctly_statistic(data):
    result = NumberOfStatuses.calculate(data)

    assert isinstance(result, Counter)
    assert result['200'] == 2
