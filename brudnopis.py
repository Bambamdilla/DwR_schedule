import random
import calendar
import datetime
from calendarium import create_calendar
from employees import doctor_list, assistant_list
from checks import can_work_together, can_work_this_day

def draw_employees():
    days_list = create_calendar()
    print(days_list)
    graph = {}
    for day in days_list:
        doctor_number = random.randrange(len(doctor_list))
        assistant_number = random.randrange(len(assistant_list))
        doctor = doctor_list[doctor_number]
        assistant = assistant_list[assistant_number]
        if can_work_this_day(day, doctor) and can_work_this_day(day, assistant):
            if can_work_together(doctor, assistant):
                graph[day] = {doctor_list[doctor_number] + assistant_list[assistant_number]}

    print(graph)


draw_employees()

# date = str(input('Enter the date(for example:09 02 2019):'))
# day_name = ['pon', 'wt', 'sr', 'czw', 'pt', 'Saturday', 'Sunday']
# day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
# print(day_name[day])


