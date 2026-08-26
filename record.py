from datetime import datetime as dt
import re

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

class Email:
    def __init__(self, email: str):
        self.email = self.validate(email)

    def __str__(self):
        return self.email

    def validate(self, email: str):
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if re.match(email_pattern, email):
            return email
        raise ValueError("Invalid email format. Use a valid email address (e.g., user@example.com).")

class Address:
    def __init__(self, address: str):
        self.address = self.validate(address)

    def __str__(self):
        return self.address

    def validate(self, address: str):
        address = address.strip()
        if address:
            return address
        raise ValueError("Address cannot be empty.")

class Record:
    def __init__(self, name: str):
        self.name = name
        self.phones: list[Phone] = []
        self.birthday = None
        self.email = None
        self.address = None
    def __str__(self):
        return (
            f"Contact name: {self.name}," 
            f" Phones: {'; '.join(p.number for p in self.phones)}, " 
            f"Birthday: {self.birthday.date if self.birthday else 'N/A'}, " 
            f"Email: {self.email.email if self.email else 'N/A'}, " 
            f"Address: {self.address.address if self.address else 'N/A'}"
            )

    # Phone methods
    def add_phone(self, phone: str):
        new_phone = Phone(phone)
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
        self.birthday = new_birthday

    def get_birthday(self):
        if self.birthday:
            return self.birthday.date
        return "N/A"

    # Email methods

    def add_email(self, email: str):
        self.email = Email(email)

    def edit_email(self, new_email: str):
        if self.email is not None:
            self.email = Email(new_email)
        else:
            raise ValueError("No email to edit. Please add an email first.")

    def get_email(self):
        if self.email is not None:
            return self.email.email
        return "N/A"

    def remove_email(self):
        if self.email is not None:
            self.email = None
        else:
            raise ValueError("No email to remove.")

    # Address methods

    def add_address(self, address: str):
        self.address = Address(address)

    def edit_address(self, new_address: str):
        if self.address is not None:
            self.address = Address(new_address)
        else:
            raise ValueError("No address to edit. Please add an address first.")
    def get_address(self):
        if self.address is not None:
            return self.address.address
        return "N/A"

    def remove_address(self):
        if self.address is not None:
            self.address = None
        else:
            raise ValueError("No address to remove.")