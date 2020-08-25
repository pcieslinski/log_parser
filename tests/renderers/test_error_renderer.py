import mock
import pytest
from io import StringIO

from log_parser.renderers import ErrorRenderer
from log_parser.renderers.irenderer import Renderer


@pytest.fixture
def renderer() -> Renderer:
    return ErrorRenderer(
            error='test_error',
            detail_error='test_detail_error',
            verbose=False,
            type='test_type'
        )


class TestErrorRenderer:

    def test_error_renderer_initialize_correctly(self, renderer):
        assert isinstance(renderer, ErrorRenderer)
        assert renderer.error == 'test_error'
        assert renderer.detailed_error == 'test_detail_error'
        assert renderer.verbose is False
        assert renderer.type == 'test_type'

    def test_error_renderer_renders_correctly_errors(self, renderer):
        with mock.patch('sys.stdout', new=StringIO()) as rendered_message:
            renderer.render()

            expected = ('test_type\ntest_error\n'
                        '\nRun with `--verbose/-v` to get more detailed error message\n')

            assert rendered_message.getvalue() == expected

    def test_error_renderer_renders_correctly_errors_in_verbose_mode(self):
        renderer = ErrorRenderer(
            error='test_error',
            detail_error='test_detail_error',
            verbose=True,
            type='test_type'
        )

        with mock.patch('sys.stdout', new=StringIO()) as rendered_message:
            renderer.render()
            assert rendered_message.getvalue() == 'test_type\ntest_detail_error\n'
