import calendar
from datetime import datetime, timedelta, date
from enum import Enum


class IntervalTypes(Enum):
    WEEK = "WEEK"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    YEAR = "YEAR"
    REVIEW = "REVIEW"


def solution(interval_type, start, end):
    result = []

    if interval_type == IntervalTypes.MONTH:
        while start <= end:
            d = start.replace(day=calendar.monthrange(start.year, start.month)[1])
            if d > end:
                d = end
            result.append([start, d])
            start = d + timedelta(days=1)
    elif interval_type == IntervalTypes.WEEK:
        while start <= end:
            idx = (start.weekday() + 1)
            current_end = start + timedelta(days=7-idx)
            if current_end > end:
                current_end = end
            result.append([start, current_end])
            start = current_end + timedelta(days=1)
    elif interval_type == IntervalTypes.QUARTER:
        while start <= end:
            current_quarter = (start.month-1)//3 + 1
            month_id = (3 * current_quarter + 1)
            last_date = start
            if month_id > 12:
                last_date = last_date.replace(year=last_date.year+1, month=1)
                month_id = 1
            last_date = date(last_date.year, month_id, 1) - timedelta(days=1)
            if last_date > end:
                last_date = end
            result.append([start, last_date])
            start = last_date + timedelta(days=1)
    elif interval_type == IntervalTypes.YEAR:
        while start <= end:
            current_year = start.year
            last_date = start.replace(year=current_year+1, month=1, day=1) - timedelta(days=1)
            if last_date > end:
                last_date = end
            result.append([start, last_date])
            start = last_date + timedelta(days=1)
    elif interval_type == IntervalTypes.REVIEW:
        # intervals = []
        while start <= end:
            if start <= date(year=start.year, month=3, day=31):
                last_date = date(year=start.year, month=3, day=31)
            elif start <= date(year=start.year, month=9, day=30):
                last_date = date(year=start.year, month=9, day=30)
            elif start >= date(year=start.year, month=10, day=1):
                last_date = date(year=start.year+1, month=3, day=31)

            if last_date > end:
                last_date = end
            result.append([start, last_date])
            start = last_date + timedelta(days=1)

    return result


if __name__ == "__main__":
    with open("input.txt", "r") as fi:
        interval_type = fi.readline().strip()
        interval = fi.readline().strip()

    date_format = "%Y-%m-%d"
    date_from, date_to = interval.split(' ')
    start = datetime.strptime(date_from, date_format).date()
    end = datetime.strptime(date_to, date_format).date()

    res = solution(IntervalTypes(interval_type), start, end)

    with open("output.txt", "w") as fo:
        fo.write(f"{len(res)}\n")
        for i in res:
            fo.write(f"{i[0]} {i[1]}\n")
