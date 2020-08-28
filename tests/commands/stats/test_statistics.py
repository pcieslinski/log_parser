from collections import Counter

import pytest

from log_parser.commands.stats.statistics import (
    AverageResponseSize,
    NumberOfRequests,
    RequestsPerSecond,
    NumberOfStatuses
)


def test_average_response_size_calculates_correctly_statistic(data):
    assert AverageResponseSize.calculate(data) == '720.0B'


@pytest.mark.parametrize('value,result', [
    (0, '0B'),
    (1024, '1.0KB'),
    (1048576, '1.0MB'),
    (1073741824, '1.0GB')

])
def test_average_response_size_converts_correctly_sizes_from_bytes(value, result):
    assert AverageResponseSize.convert_size(value) == result


def test_number_of_requests_calculates_correctly_statistic(data):
    assert NumberOfRequests.calculate(data) == 2


def test_requests_per_second_calculates_correctly_statistic(data):
    assert RequestsPerSecond.calculate(data) == 0.2


def test_number_of_statuses_calculates_correctly_statistic(data):
    result = NumberOfStatuses.calculate(data)

    assert isinstance(result, Counter)
    assert result['200'] == 2
