from address_book import AddressBook
from record import Record
from decorators import input_error_handler
from helpers import checkForArguments, checkIfRecordExists
import pickle

valid_commands = [
    "hello", "close", "exit", "add", "remove", "change", "search", "all", "phone", 
    "add_birthday", "show_birthday", "birthdays", "add_email", "edit_email", 
    "get_email", "remove_email", "add_address", "edit_address", "get_address", 
    "remove_address", "add_note", "notes", "edit_note", "remove_note"
    ]

def parse_input(user_input):
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args 

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

@input_error_handler
def add_contact(book, *args):
    checkForArguments(args, 2, ["name", "phone"])

    name, phone, *_ = args
    record = book.find(name)
    message = ""

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact added: {name}"
    else: 
        message = f"Contact updated: {name}"

    if phone:
        record.add_phone(phone)
        message += f", phone: {phone}"

    print(message)
    
@input_error_handler
def change_contact(book, *args):
    checkForArguments(args, 3, ["name", "old_phone", "new_phone"])

    name, old_phone, new_phone, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    record.edit_phone(old_phone, new_phone)

    print(f"Changing a contact phone: {name} {old_phone} -> {new_phone}")

@input_error_handler
def search_contact(book, *args):
    checkForArguments(args, 1, ["query"])

    query = args[0]
    results = book.search(query)

    if not results:
        print(f"No contacts found matching '{query}'.")
        return

    print(f"Contacts matching '{query}':")
    for record in results:
        print(record)

@input_error_handler
def remove_contact(book, *args):
    checkForArguments(args, 1, ["name"])

    name = args[0]
    record = book.find(name)

    if record is None:
        print(f"No contact found with name '{name}'.")
        return

    book.remove_record(record)
    print(f"Contact removed: {name}")   

@input_error_handler
def show_phone(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    print(f"Phone numbers for {name}:")
    for phone in record.phones:
        print(phone)

@input_error_handler
def show_all_contacts(book):
    print("Showing all contacts:")
    for record in book.data.values():
        print(record)
        print()

@input_error_handler
def add_birthday(book, *args):
    checkForArguments(args, 2, ["name", "birthday"])

    name, birthday, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    record.add_birthday(birthday)

    print(f"Adding a birthday: {name} {birthday}")

@input_error_handler
def show_birthday(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    birthday = record.get_birthday()
    print(f"Birthday for {name}: {birthday}")

@input_error_handler
def upcoming_birthdays(book, *args):
    delta = 7  # Default value if no argument is provided
    if len(args):
        try:
            delta = int(args[0])
        except ValueError:
            raise ValueError("Invalid argument for 'birthdays' command. Please provide an integer.")

    upcoming_birthdays = book.get_upcoming_birthdays(delta)

    if not upcoming_birthdays:
        print(f"No upcoming birthdays in the next {delta} days.")
        return

    print(f"Upcoming birthdays in the next {delta} days:")
    for birthday_info in upcoming_birthdays:
        name = birthday_info["name"]
        congratulation_date = birthday_info["congratulation_date"]
        print(f"{name}: {congratulation_date}")

@input_error_handler
def add_email(book, *args):
    checkForArguments(args, 2, ["name", "email"])

    name, email, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    record.add_email(email)

    print(f"Adding an email: {name} {email}")

@input_error_handler
def edit_email(book, *args):
    checkForArguments(args, 2, ["name", "new_email"])

    name, new_email, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    old_email = record.get_email()
    record.edit_email(new_email)

    print(f"Editing email: {name}: {old_email} -> {new_email}")

@input_error_handler
def get_email(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    email = record.get_email()
    print(f"Email for {name}: {email}")

@input_error_handler
def remove_email(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    record.remove_email()
    print(f"Email removed for {name}.")

@input_error_handler
def add_address(book, *args):
    checkForArguments(args, 2, ["name", "address"])

    name, *_ = args
    address = " ".join(args[1:])
    record = book.find(name)

    checkIfRecordExists(record, name)

    record.add_address(address)
    print(f"Adding an address: {name} {address}")

@input_error_handler
def edit_address(book, *args):
    checkForArguments(args, 2, ["name", "new_address"])

    name, *_ = args
    new_address = " ".join(args[1:])
    record = book.find(name)

    checkIfRecordExists(record, name)

    old_address = record.get_address()
    record.edit_address(new_address)
    print(f"Editing address: {name}: {old_address} -> {new_address}")

@input_error_handler
def get_address(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    address = record.get_address()
    print(f"Address for {name}: {address}")

@input_error_handler
def remove_address(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    record.remove_address()
    print(f"Address removed for {name}.")

# Нотатки
@input_error_handler
def add_note(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    note = input(f"Enter the Note:\n").strip()
    note_number = record.add_note(note)
    print(f"Adding Note {note_number} for contact {name}")

@input_error_handler
def show_notes(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    print(f"Notes for {name}:\n{record.notes}")

@input_error_handler
def edit_note(book, *args):
    # checkForArguments(args, 2, ["name", "note_number"])
    checkForArguments(args, 1, ["name"])
    
    name, *_ = args
    record = book.find(name)
    checkIfRecordExists(record, name)

    show_notes(book, *args)
    try:
        note_number = int(input(f"Chose Note Number to edit:\n").strip())
    except ValueError:
        raise ValueError("Invalid note number. Provide an integer.")
    
    if note_number <= 0 or note_number > len(record.notes.notes):
        raise ValueError(f"Note number {note_number} not found.")

    new_note = input(f"Enter the new Note:\n").strip()
    record.edit_note(note_number, new_note)
    print(f"Editing Note {note_number} for contact {name}")

@input_error_handler
def remove_note(book, *args):
    checkForArguments(args, 1, ["name"])
    
    name, *_ = args
    record = book.find(name)
    checkIfRecordExists(record, name)

    show_notes(book, *args)
    choice = input(f"Chose Note Number to remove or 'all':\n").strip()

    if choice == 'all':
        record.notes.notes.clear()
        print(f"All notes removed for contact {name}")
        return
    
    try:
        note_number = int(choice)
    except ValueError:
        raise ValueError("Invalid note number. Provide an integer.")
    
    if note_number <= 0 or note_number > len(record.notes.notes):
        raise ValueError(f"Note number {note_number} not found.")

    record.delete_note(note_number)
    print(f"Removing Note {note_number} for contact {name}")

def main():
    
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        command_input = input("Enter a command >>> ").strip()
        command, *args = parse_input(command_input)

        if command not in valid_commands:
            print("Invalid command. Please try again.")
            continue

        try:
            if command == "add":
                add_contact(book, *args)
            elif command == "change":
                change_contact(book, *args)
            elif command == "search":
                search_contact(book, *args)
            elif command == "remove":
                remove_contact(book, *args)
            elif command == "phone":
                show_phone(book, *args)
            elif command == "all":
                show_all_contacts(book)
            elif command == "add_birthday":
                add_birthday(book, *args)
            elif command == "show_birthday":
                show_birthday(book, *args)
            elif command == "birthdays":
                upcoming_birthdays(book, *args)
            elif command == "hello":
                print("How can I help you?")
            elif command == "add_email":
                add_email(book, *args)
            elif command == "edit_email":
                edit_email(book, *args)
            elif command == "get_email":
                get_email(book, *args)
            elif command == "remove_email":
                remove_email(book, *args)
            elif command == "add_address":
                add_address(book, *args)
            elif command == "edit_address":
                edit_address(book, *args)
            elif command == "get_address":
                get_address(book, *args)
            elif command == "remove_address":
                remove_address(book, *args)
            elif command == "add_note":
                add_note(book, *args)
            elif command == "notes":
                show_notes(book, *args)
            elif command == "edit_note":
                edit_note(book, *args)
            elif command == "remove_note":
                remove_note(book, *args)

            elif command in ["close", "exit"]:
                print("Good bye!")
                save_data(book)
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
    