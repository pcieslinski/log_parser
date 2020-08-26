from re import Pattern

from log_parser.parser.pattern_builder.ipattern_builder import IPatternBuilder


class Director:
    def __init__(self, builder: IPatternBuilder) -> None:
        self._builder = builder

    def build_pattern(self) -> None:
        self._builder.new_pattern()

        self._builder.build_prefix_component_pattern()
        self._builder.build_host_component_pattern()
        self._builder.build_identity_component_pattern()
        self._builder.build_user_component_pattern()
        self._builder.build_date_component_pattern()
        self._builder.build_request_component_pattern()
        self._builder.build_status_component_pattern()
        self._builder.build_bytes_component_pattern()
        self._builder.build_referer_component_pattern()
        self._builder.build_user_agent_component_pattern()

    def get_pattern(self) -> Pattern:
        return self._builder.get_pattern()
