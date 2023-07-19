import calendar
from consts import OFF_DAYS, HOLIDAYS


def create_calendar():
    year = int(input("Podaj rok: "))
    month = int(input("Podaj miesiąc: "))

    obj = calendar.Calendar()

    # creating calendar as list starting from Monday
    days_list = [day for day in obj.itermonthdays(year, month)]

    # removing weekends and holidays from calendar
    for i in sorted(OFF_DAYS, reverse=True):
        del days_list[i]
    for i in HOLIDAYS.get(month):
        if i in days_list:
            days_list.remove(i)
    days_list = list(filter(lambda x: x != 0, days_list))
    return days_list


print(create_calendar)
