import re
import pytest
from mock import Mock
from typing import Tuple

from log_parser.parser.pattern_builder import Director


@pytest.fixture
def mock_builder() -> Mock:
    return Mock()


@pytest.fixture
def director_with_mock_builder(mock_builder) -> Tuple[Director, Mock]:
    return Director(builder=mock_builder), mock_builder


class TestDirector:

    def test_director_initialize_correctly(self, director_with_mock_builder):
        director, mock_builder = director_with_mock_builder

        assert isinstance(director, Director)
        assert hasattr(director, '_builder')
        assert director._builder == mock_builder

    def test_build_pattern_builds_pattern(self, director_with_mock_builder):
        director, mock_builder = director_with_mock_builder

        director.build_pattern()

        mock_builder.new_pattern.assert_called_once_with()
        mock_builder.build_prefix_component_pattern.assert_called_once_with()
        mock_builder.build_host_component_pattern.assert_called_once_with()
        mock_builder.build_identity_component_pattern.assert_called_once_with()
        mock_builder.build_user_component_pattern.assert_called_once_with()
        mock_builder.build_date_component_pattern.assert_called_once_with()
        mock_builder.build_request_component_pattern.assert_called_once_with()
        mock_builder.build_status_component_pattern.assert_called_once_with()
        mock_builder.build_bytes_component_pattern.assert_called_once_with()
        mock_builder.build_referer_component_pattern.assert_called_once_with()
        mock_builder.build_user_agent_component_pattern.assert_called_once_with()

    def test_get_patterns_returns_pattern_object(self, director_with_mock_builder):
        director, mock_builder = director_with_mock_builder
        pattern = re.compile(r'')

        mock_builder.get_pattern.return_value = pattern

        result = director.get_pattern()

        mock_builder.get_pattern.assert_called_once_with()
        assert result is pattern
