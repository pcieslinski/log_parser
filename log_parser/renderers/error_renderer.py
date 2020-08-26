from typing import Any

from log_parser.renderers.irenderer import IRenderer


class ErrorRenderer(IRenderer):
    def __init__(self, error: str, detail_error: Any, verbose: bool, type: str) -> None:
        self.error = error
        self.detailed_error = detail_error
        self.verbose = verbose
        self.type = type

    def render(self) -> None:
        if self.verbose:
            print(f'{self.type}')
            print(f'{self.detailed_error}')
        else:
            print(f'{self.type}')
            print(f'{self.error}')
            if self.detailed_error != self.error and not self.verbose:
                print('\nRun with `--verbose/-v` to get more detailed error message')
