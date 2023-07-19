import employees
import datetime

def can_work_together(doctor, assistant):
    if doctor.name in assistant.excluded_people or assistant.name in doctor.excluded_people:
        print("False")
        return False
    else:
        print("True")
        return True


def can_work_this_day(day, employee):
    date =
    if day in employee.excluded_days:
        print("False")
        return False
    else:
        print("True")
        return True


date = str(input('Enter the date(for example:9 2 2019):'))
day_name = ['pon', 'wt', 'sr', 'czw', 'pt', 'Saturday', 'Sunday']
day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
print(day_name[day])

# can_work_together(employees.Gwiazda, employees.Hania)
# can_work_together(employees.Gwiazda, employees.Ass2)
# can_work_this_day("pt", employees.Hania)
# can_work_this_day("wt", employees.Hania)