from collections import Counter

from log_parser.renderers.irenderer import IRenderer


class StatsOutputRenderer(IRenderer):
    def __init__(
            self,
            n_requests: int,
            responses_statuses_count: Counter,
            requests_per_second: float,
            avg_size_for_2xx: str
    ) -> None:
        self.n_requests = n_requests
        self.responses_statuses_count = responses_statuses_count
        self.requests_per_second = requests_per_second
        self.avg_size_for_2xx = avg_size_for_2xx

    def render(self) -> None:
        print(f'Number of requests: {self.n_requests}')

        print('Responses statuses count:')
        for status, count in self.responses_statuses_count.items():
            print(f'{status}: {count}')

        print(f'Requests per second: {self.requests_per_second}')
        print(f'Average size of response for 2xx: {self.avg_size_for_2xx}')
