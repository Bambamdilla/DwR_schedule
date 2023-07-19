import random
import calendar
import datetime

import employees
from calendarium import Given_month
from employees import doctor_list, assistant_list
from checks import can_work_together, can_work_this_day, check_hours_limit

def draw_employees():
    days_list = Given_month.create_calendar_with_weekday_names()
    graph = {}
    for day in days_list.keys():
        doctor_number = random.randrange(len(doctor_list))
        assistant_number = random.randrange(len(assistant_list))
        doctor = doctor_list[doctor_number]
        assistant = assistant_list[assistant_number]
        # To do: repeat the loop if day is not covered
        if doctor.hours > 7 and assistant.hours > 7:
            if can_work_this_day(days_list.get(day), doctor) and can_work_this_day(days_list.get(day), assistant):
                if can_work_together(doctor, assistant):
                    graph[day] = {f"{doctor.name} + {assistant.name}"}
                    doctor.hours -= 8
                    assistant.hours -= 8
    print(graph)


draw_employees()



