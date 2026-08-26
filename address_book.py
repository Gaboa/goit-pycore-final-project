from datetime import datetime as dt
from record import Record

class AddressBook:
    def __init__(self):
        self.data: dict[str, Record] = {}

    def add_record(self, record):
        if record.name in self.data:
            raise ValueError("Record with this name already exists")
        self.data[record.name] = record

    def find(self, name):
        return self.data.get(name)

    def search(self, query):
        result = []
        for record in self.data.values():
            if query.lower() in record.name.lower():
                result.append(record)
        return result

    def birthdays(self):
        result = []
        for record in self.data.values():
            if record.birthday:
                result.append(f"{record.name}: {record.get_birthday()}")
        return result

    def get_upcoming_birthdays(self) -> list[Record]:
        result = []
        today = dt.today()

        for user in self.data.values():
            birthday = dt.strptime(user.get_birthday(), "%Y-%m-%d")
            delta_days = birthday.replace(year=today.year, hour=23, minute=59, second=59) - today
    
            if delta_days.days >= 0 and delta_days.days < 7:
                congratulation_date = birthday.replace(year=today.year)
                congratulation_weekday = congratulation_date.date().isoweekday()
                addditional_days = 0

                if congratulation_weekday == 6:  # Saturday
                    addditional_days = 2
                elif congratulation_weekday == 7:  # Sunday
                    addditional_days = 1

                congratulation_date = congratulation_date.replace(day=congratulation_date.day + addditional_days)

                result.append({
                    "name": user.name,
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                })

        return result

    def delete(self, name):
        record = self.find(name)
        if record:
            del self.data[record.name]
        else:
            raise ValueError("Record not found")

