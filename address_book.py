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

    def get_upcoming_birthdays(self, delta) -> list[dict]:
        result = []
        today = dt.today()

        # For 29th February birthdays, adjust to 28th February in non-leap years
        def get_birthday_for_year(birthday_dt: dt, year: int) -> dt:
            try:
                return birthday_dt.replace(year=year, hour=23, minute=59, second=59)
            except ValueError:
                return birthday_dt.replace(
                    year=year, month=2, day=28, hour=23, minute=59, second=59
                )

        for user in self.data.values():
            if user.get_birthday() != "N/A":
                birthday = dt.strptime(user.get_birthday(), "%Y-%m-%d")
                nearest_birthday = get_birthday_for_year(birthday, today.year)
                if nearest_birthday < today:
                    nearest_birthday = get_birthday_for_year(birthday, today.year + 1)

                delta_days = nearest_birthday - today

                if delta_days.days < delta:
                    congratulation_date = nearest_birthday.strftime("%Y-%m-%d")

                    result.append(
                        {
                            "name": user.name,
                            "congratulation_date": congratulation_date,
                        }
                    )

        return result

    def remove_record(self, record):
        if record.name in self.data:
            del self.data[record.name]
        else:
            raise ValueError("Record not found")
