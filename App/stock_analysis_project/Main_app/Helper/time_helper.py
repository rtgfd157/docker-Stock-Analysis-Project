import time
from datetime import datetime, date, time, timedelta


def get_current_day():
    return datetime.today()
     
def get_date_from_today():
    """
        return year, month, day object instance
    """
    today = get_current_day()
    return date(today.year, today.month, today.day)


def time_delta_after_x_days(days_delta_amount):
    """
        return day after delta amount of time
        to add: check for negative number input
        days_delta_amount need to be minus
    """


    today = get_current_day()
    today_date_only=today.date()

    day_after_days_delta_amount = today_date_only + timedelta(days=days_delta_amount)
    return day_after_days_delta_amount # return date e.g 2021-07-26


def today_date_string():
    return str(get_date_from_today())

