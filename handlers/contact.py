from utils.decorators import input_error_handler
from utils.helpers import checkForArguments, checkIfRecordExists, checkEmptyPhoneNumber
from record import Record

@input_error_handler
def add_contact(book, *args):
    checkEmptyPhoneNumber(args)
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

    checkIfRecordExists(record, name)

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

command_handler_map = {
    "add": add_contact,
    "add_contact": add_contact,
    "change": change_contact,
    "change_contact": change_contact,
    "search": search_contact,
    "search_contact": search_contact,
    "remove": remove_contact,
    "remove_contact": remove_contact,
    "phone": show_phone,
    "show_phone": show_phone,
    "all": show_all_contacts,
    "show_all_contacts": show_all_contacts
}