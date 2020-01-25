import mock
import pytest

from log_parser.request_counter import RequestCounter


@pytest.fixture
def counter():
    return RequestCounter('./test.log2')


class TestRequestCounter:

    def test_request_counter_initialize_correctly(self, counter):
        assert isinstance(counter, RequestCounter)
        assert hasattr(counter, 'file')
        assert counter.file == './test.log2'

    @pytest.mark.parametrize('data,result', [
        ('sample\nsample\nsample', 2),
        ('', 0)
    ])
    def test_count_requests_executes_correctly(self, data, result, counter):
        m = mock.mock_open(read_data=data)

        with mock.patch('builtins.open', m, create=True):
            n_requests = counter.count_requests()

            m.assert_called_once_with('./test.log2', 'r')
            assert n_requests == result

    def test_count_requests_raises_exception_when_called_with_not_existing_file(self,
                                                                                counter):
        with pytest.raises(FileNotFoundError):
            counter.count_requests()
