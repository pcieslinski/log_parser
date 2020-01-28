import mock
import pytest
from io import StringIO
from collections import Counter

from log_parser.renderers.irenderer import Renderer
from log_parser.renderers import StatsOutputRenderer


@pytest.fixture
def renderer() -> Renderer:
    return StatsOutputRenderer(
            n_requests=10,
            responses_statuses_count=Counter(['200', '200']),
            requests_per_second=1.0,
            avg_size_for_2xx='1.0MB'
        )


class TestStatsOutputRenderer:

    def test_stats_output_renderer_initialize_correctly(self, renderer):
        assert isinstance(renderer, StatsOutputRenderer)
        assert renderer.n_requests == 10
        assert renderer.responses_statuses_count == Counter(['200', '200'])
        assert renderer.requests_per_second == 1.0
        assert renderer.avg_size_for_2xx == '1.0MB'

    def test_stats_output_renderer_renders_correctly_output(self, renderer):
        with mock.patch('sys.stdout', new=StringIO()) as rendered_message:
            renderer.render()

            expected = ('Number of requests: 10\n'
                        'Responses statuses count:\n'
                        '200: 2\n'
                        'Requests per second: 1.0\n'
                        'Average size of response for 2xx: 1.0MB\n')

            assert rendered_message.getvalue() == expected
