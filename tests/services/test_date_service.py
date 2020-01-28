import pytest
import datetime as dt

from log_parser.services.date_service import DateService


@pytest.fixture
def date_service() -> DateService:
    return DateService()


class TestDateService:

    def test_date_service_initialize_correctly(self, date_service):
        assert isinstance(date_service, DateService)
        assert date_service.date_format == '%d/%b/%Y:%H:%M:%S'
        assert date_service.date_base_index == 0
        assert date_service.date_utc_index == 1

    def test_date_service_property_format_returns_date_format(self, date_service):
        assert date_service.format == '%d/%b/%Y:%H:%M:%S'

    def test_extract_date_method_extracts_date_from_log_line(self, date_service, data):
        dates = [
            date_service.extract_date(log_line)
            for log_line in data
        ]

        assert len(dates) == 2
        assert isinstance(dates[0], dt.datetime)
        assert isinstance(dates[1], dt.datetime)
        assert dates[0] == dt.datetime(2019, 11, 30, 21, 3, 13)
        assert dates[1] == dt.datetime(2019, 11, 30, 21, 3, 00)
