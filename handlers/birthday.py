from utils.decorators import input_error_handler
from utils.helpers import checkForArguments, checkIfRecordExists

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

command_handler_map = {
    "add_birthday": add_birthday,
    "show_birthday": show_birthday,
    "upcoming_birthdays": upcoming_birthdays,
    "birthdays": upcoming_birthdays
}
