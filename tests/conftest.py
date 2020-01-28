import pytest
from typing import List

from log_parser.parser.log_line import LogLine


@pytest.fixture
def log_line_data() -> List[dict]:
    return [
        dict(
            prefix='Nov 30 21:03:13 actify3-test-vm1 gunicorn[53253]',
            host='172.16.3.14',
            identity='-',
            user='-',
            date='30/Nov/2019:21:03:13 +0100',
            request='GET /internal/user/c1df9cd0-/agenda/2019-11-30/2019-12-01 HTTP/1.1',
            status='200',
            bytes='720',
            referer='-',
            user_agent='python-requests/2.22.0'
        ),
        dict(
            prefix='Nov 30 21:03:13 actify3-test-vm1 gunicorn[53253]',
            host='172.16.3.14',
            identity='-',
            user='-',
            date='30/Nov/2019:21:03:00 +0100',
            request='GET /internal/user/c1df9cd0-/agenda/2019-11-30/2019-12-01 HTTP/1.1',
            status='200',
            bytes='720',
            referer='-',
            user_agent='python-requests/2.22.0'
        )
    ]


@pytest.fixture
def data(log_line_data):
    return [
        LogLine(**data) for data in log_line_data
    ]
