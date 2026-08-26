from address_book import AddressBook
from record import Record
from decorators import input_error_handler
import pickle

valid_commands = ["hello", "close", "exit", "add", "change", "all", "phone", "add_birthday", "show_birthday", "birthdays", "add_email", "edit_email", "get_email", "remove_email", "add_address", "edit_address", "get_address", "remove_address"]

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
    if len(args) < 2:
        raise ValueError("Insufficient arguments for 'add' command. Please provide both name and phone number.")

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
    if len(args) < 3:
        raise ValueError("Insufficient arguments for 'change' command. Please provide name, old phone number, and new phone number.")

    name, old_phone, new_phone, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    record.edit_phone(old_phone, new_phone)

    print(f"Changing a contact phone: {name} {old_phone} -> {new_phone}")

@input_error_handler
def show_phone(book, *args):
    if len(args) < 1:
        raise ValueError("Insufficient arguments for 'phone' command. Please provide the name.")

    name, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    print(f"Phone numbers for {name}:")
    for phone in record.phones:
        print(phone)

@input_error_handler
def show_all_contacts(book):
    print("Showing all contacts:")
    for record in book.data.values():
        print(record)

@input_error_handler
def add_birthday(book, *args):
    if len(args) < 2:
        raise ValueError("Insufficient arguments for this command. Please provide both name and birthday.")

    name, birthday, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    record.add_birthday(birthday)

    print(f"Adding a birthday: {name} {birthday}")

@input_error_handler
def show_birthday(book, *args):
    if len(args) < 1:
        raise ValueError("Insufficient arguments for this command. Please provide the name.")

    name, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    birthday = record.get_birthday()
    print(f"Birthday for {name}: {birthday}")

@input_error_handler
def upcoming_birthdays(book, *args):
    upcoming_birthdays = book.get_upcoming_birthdays()

    if not upcoming_birthdays:
        print("No upcoming birthdays in the next 7 days.")
        return

    print("Upcoming birthdays in the next 7 days:")
    for birthday_info in upcoming_birthdays:
        name = birthday_info["name"]
        congratulation_date = birthday_info["congratulation_date"]
        print(f"{name}: {congratulation_date}")

@input_error_handler
def add_email(book, *args):
    if len(args) < 2:
        raise ValueError("Insufficient arguments for this command. Please provide both name and email.")

    name, email, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    record.add_email(email)

    print(f"Adding an email: {name} {email}")

@input_error_handler
def edit_email(book, *args):
    if len(args) < 2:
        raise ValueError("Insufficient arguments for this command. Please provide both name and new email.")

    name, new_email, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    record.edit_email(new_email)

    print(f"Editing email: {name} {new_email}")

@input_error_handler
def get_email(book, *args):
    if len(args) < 1:
        raise ValueError("Insufficient arguments for this command. Please provide the name.")

    name, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    email = record.get_email()
    print(f"Email for {name}: {email}")

@input_error_handler
def remove_email(book, *args):
    if len(args) < 1:
        raise ValueError("Insufficient arguments for this command. Please provide the name.")

    name, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    record.remove_email()
    print(f"Email removed for {name}.")

@input_error_handler
def add_address(book, *args):
    if len(args) < 2:
        raise ValueError("Insufficient arguments for this command. Please provide both name and address.")

    name, *_ = args
    address = " ".join(args[1:])
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    record.add_address(address)
    print(f"Adding an address: {name} {address}")

@input_error_handler
def edit_address(book, *args):
    if len(args) < 2:
        raise ValueError("Insufficient arguments for this command. Please provide both name and new address.")

    name, *_ = args
    new_address = " ".join(args[1:])
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    record.edit_address(new_address)
    print(f"Editing address: {name} {new_address}")

@input_error_handler
def get_address(book, *args):
    if len(args) < 1:
        raise ValueError("Insufficient arguments for this command. Please provide the name.")

    name, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    address = record.get_address()
    print(f"Address for {name}: {address}")

@input_error_handler
def remove_address(book, *args):
    if len(args) < 1:
        raise ValueError("Insufficient arguments for this command. Please provide the name.")

    name, *_ = args
    record = book.find(name)

    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

    record.remove_address()
    print(f"Address removed for {name}.")

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
            elif command in ["close", "exit"]:
                print("Good bye!")
                save_data(book)
                break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()