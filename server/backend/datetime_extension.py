from datetime import datetime, timedelta

def tomorrow():
    tomorrow = datetime.today() + timedelta(days=1)
    tomorrow.replace(hour = 0, minute=0, second=0, microsecond=0)
    return tomorrow

def yesterday():
    yesterday = datetime.today() + timedelta(days=-1)
    yesterday.replace(hour = 0, minute=0, second=0, microsecond=0)
    return yesterday

def next_sunday():
    today = datetime.today()
    next_sunday = today + timedelta(days=7 - today.weekday())
    next_sunday.replace(hour = 0, minute=0, second=0, microsecond=0)
    return next_sunday

def first_of_next_month():
    today = datetime.today()
    next_month = (today.replace(day=1) + timedelta(days=32)).replace(day=1)
    next_month.replace(hour = 0, minute=0, second=0, microsecond=0)
    return next_month
