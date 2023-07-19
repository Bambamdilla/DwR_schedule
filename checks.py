import employees


def can_work_together(doctor, assistant):
    if doctor.name in assistant.excluded_people or assistant.name in doctor.excluded_people:
        return False
    else:
        return True


def can_work_this_day(day, employee):
    if day in employee.excluded_days:
        return False
    else:
        return True
