import pytest


@pytest.fixture
def log_line_data():
    return dict(
        prefix='test_prefix',
        host='test_host',
        identity='test_identity',
        user='test_user',
        date='test_date',
        request='test_request',
        status='test_status',
        bytes='test_bytes',
        referer='test_referer',
        user_agent='test_user_agent'
    )
