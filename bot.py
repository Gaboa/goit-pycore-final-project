import pickle

from address_book import AddressBook
from handlers.address import command_handler_map as address_command_handler_map
from handlers.birthday import command_handler_map as birthday_command_handler_map
from handlers.contact import command_handler_map as contact_command_handler_map
from handlers.email import command_handler_map as email_command_handler_map
from handlers.notes import command_handler_map as notes_command_handler_map

command_handler_map = {}
command_handler_map.update(address_command_handler_map)
command_handler_map.update(birthday_command_handler_map)
command_handler_map.update(contact_command_handler_map)
command_handler_map.update(email_command_handler_map)
command_handler_map.update(notes_command_handler_map)

valid_commands = list(command_handler_map.keys())
valid_commands.extend(["hello", "close", "exit"])


def parse_input(user_input):
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def save_data(book, filename):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename, book_class):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return book_class()


def main():

    book = load_data("data/addressbook.pkl", AddressBook)
    print("Welcome to the assistant bot!")
    while True:
        command_input = input("Enter a command >>> ").strip()
        command, *args = parse_input(command_input)

        if command not in valid_commands:
            print("Invalid command. Please try again.")
            continue

        try:
            if command in command_handler_map:
                command_handler_map[command](book, *args)
            elif command == "hello":
                print("How can I help you?")
            elif command in ["close", "exit"]:
                print("Good bye!")
                save_data(book, "data/addressbook.pkl")
                break
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
