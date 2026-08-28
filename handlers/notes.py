from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

from utils.decorators import input_error_handler
from utils.helpers import checkForArguments, checkIfRecordExists

# Нотатки

def print_note(note_number, note):
    tags = ", ".join(note.tags) if note.tags else "No tags"

    formatted_note = FormattedText(
        [
            ("ansiyellow bold", f"{note_number}: "),
            ("", note.text),
            ("ansicyan", " | Tags: "),
            ("ansigreen", tags),
        ]
    )

    print_formatted_text(formatted_note)

@input_error_handler
def add_note(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    note = input("Enter the Note:\n").strip()

    tags_input = input("Enter tags for the note (comma-separated, optional):\n").strip()
    tags = (
        [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        if tags_input
        else None
    )

    note_number = record.add_note(note, tags)
    print(f"Adding Note {note_number} for contact {name}")


@input_error_handler
def show_notes(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    checkIfRecordExists(record, name)

    if not record.notes.notes:
        print(f"No notes found for contact {name}.")
        return

    print(f"Notes for contact {name}:")
    for note_number, note in record.notes.notes.items():
        print_note(note_number, note)


@input_error_handler
def edit_note(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)
    checkIfRecordExists(record, name)

    if not record.notes.notes:
        print(f"No notes found for contact {name}.")
        return

    show_notes(book, *args)

    try:
        note_number = int(input("Choose Note Number to edit:\n").strip())
    except ValueError:
        raise ValueError("Invalid note number. Please provide the correct note number.")

    if note_number <= 0 or note_number > len(record.notes.notes):
        raise ValueError(f"Note number {note_number} not found.")

    new_note = input("Enter the new Note:\n").strip()
    record.edit_note(note_number, new_note)
    edit_tags = (
        input("Would you like to edit tags for this note? (y/n): \n")
        .strip()
        .lower()
)
    if edit_tags == "y":
        tags_input = input(
            "Enter new tags for the note (comma-separated, optional): \n"
            ).strip()

        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
            record.edit_note_tags(note_number, tags)

        else:
            record.remove_note_tags(note_number)

    print(f"Editing Note {note_number} for contact {name}")

    new_note = input("Enter the new Note:\n").strip()
    record.edit_note(note_number, new_note)
    print(f"Editing Note {note_number} for contact {name}")


@input_error_handler
def search_notes_by_tag(book, *args):
    checkForArguments(args, 1, ["tag"])

    tag = args[0]
    result = False
    for record in book.data.values():
        matches = record.search_notes_by_tag(tag)
        if matches:
            result = True
            print(f"Notes with tag '{tag}' for contact {record.name}:")
            for note_number, note in matches.items():
                print_note(note_number, note)
            print()

    if not result:
        print(f"No notes found with tag '{tag}'.")


@input_error_handler
def sort_notes_by_tags(book, *args):
    notes_by_tags = {}

    for record in book.data.values():
        for note_number, note in record.notes.notes.items():
            for tag in note.tags:
                if tag not in notes_by_tags:
                    notes_by_tags[tag] = []
                notes_by_tags[tag].append((record.name, note_number, note))

    if not notes_by_tags:
        print("No notes with tags available to sort.")
        return

    print("Notes sorted by tags:")
    for tag, notes in notes_by_tags.items():
        print(f"\nTag: {tag}")
        for name, note_number, note in notes:
            print_note(note_number, note)


@input_error_handler
def remove_note(book, *args):
    checkForArguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)
    checkIfRecordExists(record, name)

    if not record.notes.notes:
        print(f"No notes found for contact {name}.")
        return

    if len(record.notes.notes) == 1:
        record.notes.notes.clear()
        print(f"Removing Note for contact {name}")
        return

    show_notes(book, *args)
    choice = input("Choose Note Number to remove or 'all':\n").strip()

    if choice == "all":
        record.notes.notes.clear()
        print(f"All notes removed for contact {name}")
        return

    try:
        note_number = int(choice)
    except ValueError:
        raise ValueError("Invalid note number. Please provide the correct note number.")

    if note_number <= 0 or note_number > len(record.notes.notes):
        raise ValueError(f"Note number {note_number} not found.")

    record.delete_note(note_number)
    print(f"Removing Note {note_number} for contact {name}")


@input_error_handler
def search_notes(book, *args):
    checkForArguments(args, 1, ["keys"])
    keys = " ".join(args)

    result = False
    for record in book.data.values():
        matches = record.search_notes(keys)
        if matches:
            result = True
            print(f"Notes for contact {record.name}:")
            for note_number, note in matches.items():
                print_note(note_number, note)
            print()

    if not result:
        print("No matches found.")


command_handler_map = {
    "add_note": add_note,
    "show_notes": show_notes,
    "notes": show_notes,
    "edit_note": edit_note,
    "remove_note": remove_note,
    "search_notes": search_notes,
    "search_notes_by_tag": search_notes_by_tag,
    "sort_notes_by_tags": sort_notes_by_tags,
}
