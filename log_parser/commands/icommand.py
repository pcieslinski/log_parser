from argparse import Namespace
from abc import ABC, abstractmethod


class ICommand(ABC):

    @abstractmethod
    def run(self, args: Namespace):
        pass
