from consts import WORKING_DAYS

doctor_list = []
assistant_list = []


class Employee:
    def __init__(self, name, status, hours, excluded_days, excluded_people, place, holiday):
        self.name = name
        self.status = status
        self.hours = hours
        self.excluded_days = excluded_days
        self.excluded_people = excluded_people
        self.place = place
        self.holiday = holiday
        if self.status == "doctor":
            doctor_list.append(self)
        elif self.status == "assistant":
            assistant_list.append(self)

    def change_name(self):
        self.name = input(f"Podaj nowe imię dla {self.name}: ")

    def change_hours(self):
        self.hours = int(input(f"Podaj nowy wymiar godzin dla {self.name}: "))
        print(f"Nowy wymiar godzin dla {self.name} to {self.hours} godzin w miesiącu.")

    def excluded_days_add(self, day):
        try:
            if day in self.excluded_days:
                print(f"{day} już znajduje się na liście!")
            elif day in WORKING_DAYS:
                self.excluded_days.append(day)
                print(f"Lista dni, w które {self.name} nie pracuje: {self.excluded_days}")
            else:
                print(f"Możesz dodać tylko jeden z następujących dni: {WORKING_DAYS}")
        except ValueError:
            print(f"Możesz dodać tylko jeden z następujących dni: {WORKING_DAYS}")

    def excluded_days_remove(self, day):
        try:
            if day in self.excluded_days:
                self.excluded_days.remove(day)
            else:
                print(f"Możesz dodać tylko jeden z następujących dni: {WORKING_DAYS}")
        except ValueError:
            print(f"Możesz usunąć tylko jeden z następujących dni: {self.excluded_days}")
        print(f"Lista dni, w które {self.name} nie pracuje: {self.excluded_days}")

    def excluded_people_add(self, excluded_person_name):
        try:
            if excluded_person_name.name not in self.excluded_people:
                self.excluded_people.append(excluded_person_name.name)
            else:
                print(f"{excluded_person_name.name} już znajduje się na liście!")
        except NameError:  # nie działa, zinwestygować
            print("Nie ma takiej osoby!")
        finally:
            print(f"Lista osób, z którymi {self.name} nie pracuje: {self.excluded_people}")

    def excluded_people_remove(self, included_person_name):
        try:
            if included_person_name.name in self.excluded_people:
                self.excluded_people.remove(included_person_name.name)
            else:
                print(f"{included_person_name} nie znajduje się na liście!")
        except Exception:  # nie działa, zinwestygować
            print("Nie ma takiej osoby!")
        finally:
            print(f"Lista osób, z którymi {self.name} nie pracuje: {self.excluded_people}")

    def change_place(self):
        if self.place == "Reda":
            self.place = "Rumia"
            print(f"Od teraz {self.name} pracuje w Rumi.")
        elif self.place == "Rumia":
            self.place = "Redia"
            print(f"Od teraz {self.name} pracuje w Redzie.")

    def holiday_add(self):
        try:
            start_date = int(input("Podaj pierwszy dzień urlopu: "))
            end_date = int(input("Podaj ostatni dzień urlopu: "))
            self.holiday = [x - 1 for x in range(start_date, end_date + 1)]  # counting in calendar starts from 0
        except ValueError:
            print("Podaj same liczby!")
            exit()
        print(f"{self.name} przebywać będzie na urlopie od {start_date} do {end_date}")


Gwiazda = Employee("Agnieszka G.", "doctor", 160, ["pon", "wt"], [], "Reda", False)
Lekarz2 = Employee("Lekarz2", "doctor", 160, [], [], "Reda", False)
Lekarz3 = Employee("Lekarz3", "doctor", 160, [], [], "Rumia", False)

Hania = Employee("Hanna H.", "assistant", 80, ["pon", "wt"], [Gwiazda.name], "Reda", False)
Ass2 = Employee("Asystentka2", "assistant", 80, ["pt"], [Lekarz2.name], "Reda", False)
Ass3 = Employee("Asystentka3", "assistant", 160, [], [], "Rumia", False)

#
# Gwiazda.holiday_add()
#
# print(Gwiazda.holiday)

# print(doctor_list)
