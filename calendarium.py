import calendar
import datetime
from consts import OFF_DAYS, WORKING_DAYS, HOLIDAYS


class CalendarWizard:
    def __init__(self, month, year):
        self.days_list = None
        self.month = month
        self.year = year

    def create_calendar(self):
        obj = calendar.Calendar()
        # creating calendar as list starting from Monday
        self.days_list = [day for day in obj.itermonthdays(self.year, self.month)]
        # removing weekends and holidays from calendar
        for i in sorted(OFF_DAYS, reverse=True):
            del self.days_list[i]
        for i in HOLIDAYS.get(self.month):
            if i in self.days_list:
                self.days_list.remove(i)
        # Weekdays before 1st day of month are stored as 0, so we need to get rid of them
        self.days_list = list(filter(lambda x: x != 0, self.days_list))
        return self.days_list

    def create_calendar_with_weekday_names(self):
        self.days_list = self.create_calendar()
        days_list_with_weekday_names = {}
        day_name = WORKING_DAYS
        for day in self.days_list:
            date = f"{day} {self.month} {self.year}"
            weekday = datetime.datetime.strptime(date, '%d %m %Y').weekday()
            days_list_with_weekday_names[day] = day_name[weekday]

        return days_list_with_weekday_names


Given_month = CalendarWizard(8, 2023)