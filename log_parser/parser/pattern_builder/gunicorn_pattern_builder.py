from log_parser.parser.pattern_builder.ipattern_builder import IPatternBuilder


class GunicornPatternBuilder(IPatternBuilder):

    def build_prefix_component_pattern(self) -> None:
        self._patterns.append(
            r'(?P<prefix>.*?):\s'
        )

    def build_host_component_pattern(self) -> None:
        self._patterns.append(
            r'(?P<host>[\d\.]+)\s'
        )

    def build_identity_component_pattern(self):
        self._patterns.append(
            r'(?P<identity>\S*)\s'
        )

    def build_user_component_pattern(self):
        self._patterns.append(
            r'(?P<user>\S*)\s'
        )

    def build_date_component_pattern(self):
        self._patterns.append(
            r'\[(?P<date>.*?)\]\s'
        )

    def build_request_component_pattern(self):
        self._patterns.append(
            r'"(?P<request>.*?)"\s'
        )

    def build_status_component_pattern(self):
        self._patterns.append(
            r'(?P<status>\d+)\s'
        )

    def build_bytes_component_pattern(self):
        self._patterns.append(
            r'(?P<bytes>\S*)\s'
        )

    def build_referer_component_pattern(self):
        self._patterns.append(
            r'"(?P<referer>.*?)"\s'
        )

    def build_user_agent_component_pattern(self):
        self._patterns.append(
            r'"(?P<user_agent>.*?)"\s*'
        )
