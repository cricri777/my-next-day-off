import holidays
from datetime import datetime, timedelta


def next_day_off(today_input=datetime.today()):
    ca_holidays = holidays.country_holidays("CA")
    day_off_found = False
    next_day = today_input

    while not day_off_found:
        next_day += timedelta(days=1)
        if next_day.weekday() >= 5 or next_day in ca_holidays:
            day_off_found = True

    return next_day


if __name__ == "__main__":
    today = datetime.now()
    next_off = next_day_off(today)
    print(f"The next day off is: {next_off.strftime('%Y-%m-%d')} ({next_off.strftime('%A')})")
