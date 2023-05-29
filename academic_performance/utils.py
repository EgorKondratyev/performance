import calendar
import datetime


def get_days(year, month):
    num_days = calendar.monthrange(year, month)[1]
    dates = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    return dates
