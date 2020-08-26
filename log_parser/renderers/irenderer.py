from abc import ABC, abstractmethod


class IRenderer(ABC):

    @abstractmethod
    def render(self) -> None:
        pass
