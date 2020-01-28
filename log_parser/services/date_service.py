import datetime as dt

from log_parser.parser.log_line import LogLine


class DateService:
    date_format = '%d/%b/%Y:%H:%M:%S'
    date_base_index = 0
    date_utc_index = 1

    def extract_date(self, log_line: LogLine) -> dt.datetime:
        date = log_line.date.split(' ')[self.date_base_index]
        return dt.datetime.strptime(date, self.date_format)

    @property
    def format(self):
        return self.date_format
