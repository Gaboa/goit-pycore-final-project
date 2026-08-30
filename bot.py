import pickle
from pathlib import Path

from prompt_toolkit import PromptSession

from address_book import AddressBook
from completer import create_autocomplete_bindings, find_command
from handlers.address import command_handler_map as address_command_handler_map
from handlers.birthday import command_handler_map as birthday_command_handler_map
from handlers.contact import command_handler_map as contact_command_handler_map
from handlers.email import command_handler_map as email_command_handler_map
from handlers.notes import command_handler_map as notes_command_handler_map
from hints_collection import HELP_FLAG, help_hints
from utils.options import get_all_help_hints, get_help_hint

command_handler_map = {}
command_handler_map.update(address_command_handler_map)
command_handler_map.update(birthday_command_handler_map)
command_handler_map.update(contact_command_handler_map)
command_handler_map.update(email_command_handler_map)
command_handler_map.update(notes_command_handler_map)

valid_commands = list(command_handler_map.keys())
valid_commands.extend(["hello", "close", "exit", "help"])
valid_options = [HELP_FLAG]

DATA_FILE = Path.home() / "assistant-bot" / "addressbook.pkl"


def parse_input(user_input):
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def save_data(book, filename):
    filename.parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename, book_class):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return book_class()


def main():
    book = load_data(DATA_FILE, AddressBook)

    bindings = create_autocomplete_bindings(valid_commands, valid_options)
    session = PromptSession(key_bindings=bindings)

    print("Welcome to the assistant bot!")
    while True:
        try:
            command_input = session.prompt("Enter a command >>> ").strip()
            command, *args = parse_input(command_input)

            if command not in valid_commands:
                potential_commands = find_command(command, valid_commands)

                if potential_commands:
                    print(f"Possible commands: {', '.join(potential_commands)}")
                else:
                    print("Invalid command. Please try again.")

                continue

            if args == [HELP_FLAG]:
                print(get_help_hint(command, help_hints))

                continue

            if command in command_handler_map:
                command_handler_map[command](book, *args)
            elif command == "help":
                print(get_all_help_hints(help_hints))
            elif command == "hello":
                print("How can I help you?")
            elif command in ["close", "exit"]:
                print("Good bye!")
                save_data(book, DATA_FILE)
                break
        except KeyboardInterrupt:
            print("\nInterrupted. Saving data before exit...")
            save_data(book, DATA_FILE)
            print("Good bye!")
            break
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
