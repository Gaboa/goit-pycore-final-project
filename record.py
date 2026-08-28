import re
from datetime import datetime as dt


class Phone:
    def __init__(self, number: str):
        self.number = self.validate(number)

    def __str__(self):
        return self.number

    def validate(self, number: str):
        if number.isdigit() and len(number) == 10:
            return number
        elif not number.isdigit():
            raise ValueError(
                "Phone number cannot contain letters or special characters."
            )
        raise ValueError(
            "Invalid phone number format, must be 10 digits. You have: "
            f"{len(number)} digits."
        )


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
        raise ValueError(
            "Invalid email format. Use a valid email address (e.g., user@example.com)."
        )


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


class Note:
    def __init__(self, text: str, tags=None):
        self.text = text.strip()
        self.tags = []

        if tags:
            self.add_tags(tags)

    def add_tags(self, tags):
        for tag in tags:
            tag = tag.strip().lower()
            if tag and tag not in self.tags:
                self.tags.append(tag)

    def __str__(self):
        tags = ", ".join(self.tags) if self.tags else "No tags"
        return f"{self.text} | Tags: {tags}"


class Notes:
    def __init__(self, notes: dict):
        self.notes: dict[int, Note] = notes if notes is not None else {}

    def add(self, text, tags=None):
        note_number = len(self.notes) + 1
        self.notes[note_number] = Note(text, tags)
        return note_number

    def edit_tags(self,tags):
        self.tags = []
        self.add_tags(tags)

    def remove_tags(self):
        self.tags.clear()

    def __str__(self):
        if not self.notes:
            return "No notes available."
        return "\n".join(f"{n}: {note}" for n, note in self.notes.items())

    def short(self):
        if not self.notes:
            return "N/A"
        notes_list = list(self.notes.values())
        if len(notes_list) == 1:
            return str(notes_list[0])
        return f"{notes_list[0]} and {len(notes_list) - 1} more"

    def delete(self, note_number):
        if note_number not in self.notes:
            raise ValueError(f"Note number {note_number} not found.")

        del self.notes[note_number]

        renumber = {}
        for i, (old_k, note) in enumerate(self.notes.items(), start=1):
            renumber[i] = note
        self.notes = renumber

    def search(self, keys):
        keys = re.sub(r"[^\w\s]", "", keys).lower()
        return {
            n: note
            for n, note in self.notes.items()
            if keys in re.sub(r"[^\w\s]", "", note.text).lower()
        }

    def search_by_tag(self, tag):
        tag = tag.strip().lower()
        return {number: note for number, note in self.notes.items() if tag in note.tags}


class Record:
    def __init__(self, name: str):
        self.name = name
        self.phones: list[Phone] = []
        self.birthday = None
        self.email = None
        self.address = None
        self.notes = Notes({})

    def __str__(self):
        return (
            f"Contact name: {self.name}\n"
            f"Phones: {'; '.join(p.number for p in self.phones)}\n"
            f"Birthday: {self.birthday.date if self.birthday else 'N/A'}\n"
            f"Email: {self.email.email if self.email else 'N/A'}\n"
            f"Address: {self.address.address if self.address else 'N/A'}\n"
            f"Notes: {self.notes.short() if self.notes else 'N/A'}"
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

    # Notes methods

    def add_note(self, text: str, tags=None):
        return self.notes.add(text, tags)

    def edit_note(self, note_number, new_note):
        if note_number in self.notes.notes:
            self.notes.notes[note_number].text = new_note.strip()
        else:
            raise ValueError(f"Note number {note_number} not found.")

    def edit_note_tags(self, note_number, tags):
        if note_number in self.notes.notes:
            self.notes.notes[note_number].edit_tags(tags)
        else:
            raise ValueError(f"Note number {note_number} not found.")

    def remove_note_tags(self, note_number):
        if note_number in self.notes.notes:
            self.notes.notes[note_number].remove_tags()
        else:
            raise ValueError(f"Note number {note_number} not found.")

    def delete_note(self, note_number):
        if self.notes is not None:
            self.notes.delete(note_number)

    def search_notes(self, keys):
        if self.notes is not None:
            return self.notes.search(keys)
        return {}

    def search_notes_by_tag(self, tag):
        if self.notes is not None:
            return self.notes.search_by_tag(tag)
        return {}
