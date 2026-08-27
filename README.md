# 📒 Personal Assistant Bot

Our team project written in **Python** 🐍

It's a simple CLI assistant for keeping contacts and their information in one place — phone numbers, emails, addresses, birthdays, and notes.

The data is saved between sessions, so thankfully you don't need to add everyone again after restarting the bot 😄

---

## ✨ Features

The bot can:

- 👤 Add, edit, search, and remove contacts
- 📞 Manage phone numbers
- 📧 Manage emails
- 🏠 Manage addresses
- 🎂 Save birthdays and show upcoming ones
- 📝 Add, edit, remove, and search notes
- 🔍 Search contacts by name
- ✅ Validate entered data
- 💾 Save the address book using `pickle`

---

## 📁 Project Structure

```text
project/
│
├── data/
│   └── addressbook.pkl
│
├── handlers/
│   ├── address.py
│   ├── birthday.py
│   ├── contact.py
│   ├── email.py
│   └── notes.py
│
├── utils/
│   ├── decorators.py
│   └── helpers.py
│
├── .gitignore
├── address_book.py
├── bot.py
├── record.py
└── README.md
```

We separated the handlers and utilities into folders to keep the project easier to navigate and avoid one huge `bot.py` 😅

---

## 🚀 How to Run

Clone the repository and open the project folder.

Then run:

```bash
python bot.py
```

You should see:

```text
Welcome to the assistant bot!
Enter a command >>>
```

And you're ready to go! 🚀

---

## 💬 Commands

### 👤 Contacts

| Command                                 | What it does                 |
| --------------------------------------- | ---------------------------- |
| `add <name> <phone>`                    | Add a new contact            |
| `change <name> <old_phone> <new_phone>` | Change a phone number        |
| `phone <name>`                          | Show contact's phone numbers |
| `search <query>`                        | Search contacts by name      |
| `remove <name>`                         | Remove a contact             |
| `all`                                   | Show all contacts            |

**Example:**

```text
add Alice 0123456789
```

---

### 📧 Email

| Command                         | What it does    |
| ------------------------------- | --------------- |
| `add_email <name> <email>`      | Add an email    |
| `edit_email <name> <new_email>` | Edit an email   |
| `get_email <name>`              | Show an email   |
| `remove_email <name>`           | Remove an email |

**Example:**

```text
add_email Alice alice@example.com
```

---

### 🏠 Address

| Command                             | What it does      |
| ----------------------------------- | ----------------- |
| `add_address <name> <address>`      | Add an address    |
| `edit_address <name> <new_address>` | Edit an address   |
| `get_address <name>`                | Show an address   |
| `remove_address <name>`             | Remove an address |

Addresses can contain several words:

```text
add_address Alice 15 Sunset Street Barcelona
```

---

### 🎂 Birthdays

Birthday format: **`YYYY-MM-DD`**

| Command                          | What it does                         |
| -------------------------------- | ------------------------------------ |
| `add_birthday <name> <birthday>` | Add a birthday                       |
| `show_birthday <name>`           | Show contact's birthday              |
| `birthdays`                      | Show birthdays for the next 7 days   |
| `birthdays <days>`               | Show birthdays for a selected period |

**Examples:**

```text
add_birthday Alice 1995-07-21
birthdays 30
```

---

### 📝 Notes

| Command                  | What it does            |
| ------------------------ | ----------------------- |
| `add_note <name>`        | Add a note              |
| `notes <name>`           | Show notes              |
| `edit_note <name>`       | Edit a note             |
| `remove_note <name>`     | Remove one or all notes |
| `search_notes <keyword>` | Search through notes    |

For adding, editing, and removing notes, the bot will ask for the necessary information after the command.

---

### 👋 Other Commands

| Command | What it does                    |
| ------- | ------------------------------- |
| `hello` | Say hello to the bot 👋         |
| `exit`  | Save data and close the program |
| `close` | Save data and close the program |

---

## ✅ Validation

A few rules to keep our address book under control:

- 📞 **Phone number:** exactly 10 digits
- 📧 **Email:** valid email format
- 🎂 **Birthday:** `YYYY-MM-DD`
- 🏠 **Address:** can't be empty

Incorrect input will show an error instead of crashing the program. Hopefully 😄

---

## 💾 Saving Data

Contacts are stored in:

```text
data/addressbook.pkl
```

The address book is loaded when the bot starts and saved when you use `exit` or `close`.

So basically:

> **add stuff → exit → come back later → stuff is still there** 🎉

---

## 🛠️ Built With

**Python** • **OOP** • **Decorators** • **Regex** • **Datetime** • **Pickle** • **Git & GitHub**

Made as a team project while learning Python, working with Git, fixing bugs, and occasionally creating new ones in the process 😅
