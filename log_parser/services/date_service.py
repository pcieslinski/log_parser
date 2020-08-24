import datetime as dt

from log_parser.parser.log_line import LogLine


class DateService:
    DATE_FORMAT = '%d/%b/%Y:%H:%M:%S'
    DATE_BASE_INDEX = 0
    DATE_UTC_INDEX = 1

    def extract_date(self, log_line: LogLine) -> dt.datetime:
        date = log_line.date.split(' ')[self.DATE_BASE_INDEX]
        return dt.datetime.strptime(date, self.DATE_FORMAT)

    @property
    def format(self):
        return self.DATE_FORMAT
