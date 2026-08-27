from utils.decorators import input_error_handler
from utils.helpers import checkForArguments, checkIfRecordExists

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

@input_error_handler
def search_notes(book, *args):
    checkForArguments(args, 1, ['keys'])
    keys = ' '.join(args)

    result = False
    for record in book.data.values():
        matches = record.search_notes(keys)
        if matches:
            result = True
            print(f"Notes for {record.name}:")
            for note_number, note in matches.items():
                print(f"{note_number}: {note}")
            print()

    if not result:
        print("No matches found.")

command_handler_map = {
    "add_note": add_note,
    "show_notes": show_notes,
    "notes": show_notes,
    "edit_note": edit_note,
    "remove_note": remove_note,
    "search_notes": search_notes
}
