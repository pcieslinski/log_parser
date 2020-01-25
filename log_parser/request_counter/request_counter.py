class RequestCounter:
    def __init__(self, file_path: str) -> None:
        self.file = file_path

    def count_requests(self) -> int:
        with open(self.file, 'r') as f:
            n = 0
            for n, line in enumerate(f):
                pass

            return n
