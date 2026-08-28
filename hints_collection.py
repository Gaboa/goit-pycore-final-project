HELP_FLAG = "--help"


ADD_CONTACT_HELP = """Add a new contact or add a phone to an existing contact.
Usage: add <name> <phone>
Example: add John 0123456789
The phone number must contain exactly 10 digits."""

CHANGE_CONTACT_HELP = """Change an existing phone number for a contact.
Usage: change <name> <old_phone> <new_phone>
Example: change John 0123456789 0987654321"""

SEARCH_CONTACT_HELP = """Search for contacts by name.
Usage: search <query>
Example: search John"""

REMOVE_CONTACT_HELP = """Remove a contact from the address book.
Usage: remove <name>
Example: remove John"""

SHOW_PHONE_HELP = """Show all phone numbers saved for a contact.
Usage: phone <name>
Example: phone John"""

SHOW_ALL_CONTACTS_HELP = """Show all contacts in the address book.
Usage: all"""

ADD_ADDRESS_HELP = """Add an address to an existing contact.
Usage: add_address <name> <address>
Example: add_address John 15 Sunset Street"""

EDIT_ADDRESS_HELP = """Change the address of an existing contact.
Usage: edit_address <name> <new_address>
Example: edit_address John 20 Green Street"""

GET_ADDRESS_HELP = """Show the address saved for a contact.
Usage: get_address <name>
Example: get_address John"""

REMOVE_ADDRESS_HELP = """Remove the address saved for a contact.
Usage: remove_address <name>
Example: remove_address John"""

ADD_EMAIL_HELP = """Add an email address to an existing contact.
Usage: add_email <name> <email>
Example: add_email John john@example.com"""

EDIT_EMAIL_HELP = """Change the email address of an existing contact.
Usage: edit_email <name> <new_email>
Example: edit_email John new.john@example.com"""

GET_EMAIL_HELP = """Show the email address saved for a contact.
Usage: get_email <name>
Example: get_email John"""

REMOVE_EMAIL_HELP = """Remove the email address saved for a contact.
Usage: remove_email <name>
Example: remove_email John"""

ADD_BIRTHDAY_HELP = """Add a birthday to an existing contact.
Usage: add_birthday <name> <YYYY-MM-DD>
Example: add_birthday John 1990-05-21"""

SHOW_BIRTHDAY_HELP = """Show the birthday saved for a contact.
Usage: show_birthday <name>
Example: show_birthday John"""

UPCOMING_BIRTHDAYS_HELP = """Show birthdays occurring within a number of days.
Usage: birthdays [days]
Example: birthdays 30
If days is omitted, the bot uses 7 days."""

ADD_NOTE_HELP = """Add a note to an existing contact.
Usage: add_note <name>
Example: add_note John
The bot will ask for the note text and optional tags."""

SHOW_NOTES_HELP = """Show all notes saved for a contact.
Usage: notes <name>
Example: notes John"""

EDIT_NOTE_HELP = """Edit one of a contact's notes.
Usage: edit_note <name>
Example: edit_note John
The bot will ask which note to edit and request its new text."""

REMOVE_NOTE_HELP = """Remove one or all notes saved for a contact.
Usage: remove_note <name>
Example: remove_note John
The bot may ask which note to remove."""

SEARCH_NOTES_HELP = """Search notes by text.
Usage: search_notes <keyword>
Example: search_notes meeting"""

SEARCH_NOTES_BY_TAG_HELP = """Search notes by tag.
Usage: search_notes_by_tag <tag>
Example: search_notes_by_tag work"""

SORT_NOTES_BY_TAGS_HELP = """Group and show all notes by their tags.
Usage: sort_notes_by_tags"""

HELLO_HELP = """Display the bot's greeting.
Usage: hello"""

EXIT_HELP = """Save the address book and close the bot.
Usage: exit"""


help_hints = {
    "add": ADD_CONTACT_HELP,
    "add_contact": ADD_CONTACT_HELP,
    "change": CHANGE_CONTACT_HELP,
    "change_contact": CHANGE_CONTACT_HELP,
    "search": SEARCH_CONTACT_HELP,
    "search_contact": SEARCH_CONTACT_HELP,
    "remove": REMOVE_CONTACT_HELP,
    "remove_contact": REMOVE_CONTACT_HELP,
    "phone": SHOW_PHONE_HELP,
    "show_phone": SHOW_PHONE_HELP,
    "all": SHOW_ALL_CONTACTS_HELP,
    "show_all_contacts": SHOW_ALL_CONTACTS_HELP,
    "add_address": ADD_ADDRESS_HELP,
    "edit_address": EDIT_ADDRESS_HELP,
    "get_address": GET_ADDRESS_HELP,
    "remove_address": REMOVE_ADDRESS_HELP,
    "add_email": ADD_EMAIL_HELP,
    "edit_email": EDIT_EMAIL_HELP,
    "get_email": GET_EMAIL_HELP,
    "remove_email": REMOVE_EMAIL_HELP,
    "add_birthday": ADD_BIRTHDAY_HELP,
    "show_birthday": SHOW_BIRTHDAY_HELP,
    "upcoming_birthdays": UPCOMING_BIRTHDAYS_HELP,
    "birthdays": UPCOMING_BIRTHDAYS_HELP,
    "add_note": ADD_NOTE_HELP,
    "show_notes": SHOW_NOTES_HELP,
    "notes": SHOW_NOTES_HELP,
    "edit_note": EDIT_NOTE_HELP,
    "remove_note": REMOVE_NOTE_HELP,
    "search_notes": SEARCH_NOTES_HELP,
    "search_notes_by_tag": SEARCH_NOTES_BY_TAG_HELP,
    "sort_notes_by_tags": SORT_NOTES_BY_TAGS_HELP,
    "hello": HELLO_HELP,
    "close": EXIT_HELP,
    "exit": EXIT_HELP,
}
