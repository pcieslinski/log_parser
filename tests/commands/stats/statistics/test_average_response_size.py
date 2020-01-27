import pytest

from log_parser.commands.stats.statistics import AverageResponseSize


class TestAverageResponseSize:

    def test_average_response_size_calculates_correctly_statistic(self, data):
        assert AverageResponseSize.calculate(data) == '720.0B'

    @pytest.mark.parametrize('value,result', [
        (0, '0B'),
        (1024, '1.0KB'),
        (1048576, '1.0MB'),
        (1073741824, '1.0GB')

    ])
    def test_convert_size_converts_correctly_sizes_from_bytes(self, value, result):
        assert AverageResponseSize.convert_size(value) == result
