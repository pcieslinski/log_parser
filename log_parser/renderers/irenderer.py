from typing import NewType
from abc import ABC, abstractmethod


class IRenderer(ABC):

    @abstractmethod
    def render(self, *args, **kwargs) -> None:
        pass


Renderer = NewType('Renderer', IRenderer)
