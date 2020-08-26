import re
import pytest

from log_parser.parser.pattern_builder import GunicornPatternBuilder
from log_parser.parser.pattern_builder.ipattern_builder import IPatternBuilder


@pytest.fixture
def builder() -> IPatternBuilder:
    builder = GunicornPatternBuilder()
    builder.new_pattern()
    return builder


class TestGunicornPatternBuilder:

    def test_gunicorn_pattern_builder_initialize_correctly(self):
        builder = GunicornPatternBuilder()

        assert isinstance(builder, GunicornPatternBuilder)
        assert not hasattr(builder, '_patterns')

    def test_new_pattern_creates_attribute__patterns_in_builder(self, builder):
        assert hasattr(builder, '_patterns')
        assert builder._patterns == []

    def test_get_patterns_returns_empty_pattern_when_called_with_no_components_patterns(self,
                                                                                        builder):
        pattern = builder.get_pattern()

        assert isinstance(pattern, re.Pattern)
        assert pattern == re.compile(r'')

    def test_build_prefix_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_prefix_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'(?P<prefix>.*?):\s'

    def test_build_host_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_host_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'(?P<host>[\d\.]+)\s'

    def test_build_identity_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_identity_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'(?P<identity>\S*)\s'

    def test_build_user_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_user_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'(?P<user>\S*)\s'

    def test_build_date_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_date_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'\[(?P<date>.*?)\]\s'

    def test_build_request_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_date_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'\[(?P<date>.*?)\]\s'

    def test_build_status_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_status_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'(?P<status>\d+)\s'

    def test_build_bytes_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_bytes_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'(?P<bytes>\S*)\s'

    def test_build_referer_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_referer_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'"(?P<referer>.*?)"\s'

    def test_build_user_agent_component_pattern_appends_pattern_to__patterns_attribute(self, builder):
        builder.build_user_agent_component_pattern()

        assert len(builder._patterns) == 1
        assert builder._patterns[0] == r'"(?P<user_agent>.*?)"\s*'
