from datetime import datetime as dt

class Phone:
    def __init__(self, number: str):
        self.number = self.validate(number)

    def __str__(self):
        return self.number

    def validate(self, number: str):
        if number.isdigit() and len(number) == 10:
            return number
        raise ValueError(f"Invalid phone number format, must be 10 digits. You have: {len(number)} digits.")

class Birthday:
    def __init__(self, date: str):
        self.date = self.validate(date)

    def __str__(self):
        return self.date

    def validate(self, date: str):
        try:
            dt.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError("Invalid birthday format. Use YYYY-MM-DD.")

class Record:
    def __init__(self, name: str):
        self.name = name
        self.phones: list[Phone] = []
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name}, Phones: {'; '.join(p.number for p in self.phones)} Birthday: {self.birthday.date if self.birthday else 'N/A'}"

    # Phone methods
    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        if new_phone.number:
            self.phones.append(new_phone)

    def edit_phone(self, old_number: str, new_number: str):
        phone = self.find_phone(old_number)
        if phone:
            phone.number = Phone(new_number).number
        else:
            raise ValueError(f"Phone number not found in record: {old_number}")

    def find_phone(self, number: str):
        for phone in self.phones:
            if phone.number == number:
                return phone

    def remove_phone(self, phone: str):
        phone_obj = Phone(phone)
        for p in self.phones:
            if str(p) == str(phone_obj):
                self.phones.remove(p)
                return
        raise ValueError(f"Phone number not found in record: {phone}")

    # Birthday methods
    def add_birthday(self, birthday: str):
        new_birthday = Birthday(birthday)
        if new_birthday.date:
            self.birthday = new_birthday

    def get_birthday(self):
        if self.birthday:
            return self.birthday.date
        return "N/A"