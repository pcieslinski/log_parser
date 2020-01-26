import re
from typing import NewType
from abc import ABC, abstractmethod


class IPatternBuilder(ABC):
    def get_pattern(self) -> re.Pattern:
        return re.compile(''.join(self._patterns))

    def new_pattern(self) -> None:
        self._patterns = []

    @abstractmethod
    def build_prefix_component_pattern(self) -> None:
        pass

    @abstractmethod
    def build_host_component_pattern(self) -> None:
        pass

    @abstractmethod
    def build_identity_component_pattern(self) -> None:
        pass

    @abstractmethod
    def build_user_component_pattern(self) -> None:
        pass

    @abstractmethod
    def build_date_component_pattern(self) -> None:
        pass

    @abstractmethod
    def build_request_component_pattern(self) -> None:
        pass

    @abstractmethod
    def build_status_component_pattern(self) -> None:
        pass

    @abstractmethod
    def build_bytes_component_pattern(self) -> None:
        pass

    @abstractmethod
    def build_referer_component_pattern(self) -> None:
        pass

    @abstractmethod
    def build_user_agent_component_pattern(self) -> None:
        pass


PatternBuilder = NewType('PatternBuilder', IPatternBuilder)
