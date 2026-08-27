from utils.decorators import input_error_handler
from utils.helpers import checkForArguments, checkIfRecordExists

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

command_handler_map = {
    "add_email": add_email,
    "edit_email": edit_email,
    "get_email": get_email,
    "remove_email": remove_email
}