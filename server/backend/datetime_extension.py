from datetime import datetime, timedelta

def tomorrow():
    return datetime.today() + timedelta(days=1)

def yesterday():
    return datetime.today() + timedelta(days=-1)

def next_sunday():
    today = datetime.today()
    return today + timedelta(days=7 - today.weekday())

def first_of_next_month():
    today = datetime.today()
    return (today.replace(day=1) + timedelta(days=32)).replace(day=1)
