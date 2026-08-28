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
- ⌨️ Suggest matching commands when you press `Tab`
- 💡 Show command instructions with `--help` or `help`
- ✅ Validate entered data
- 💾 Save the address book using `pickle`

---

## 📁 Project Structure

```text
project/
│
├── .github/
│   └── workflows/
│       └── lint.yml
│
├── .vscode/
│   ├── extensions.json
│   └── settings.json
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
│   ├── helpers.py
│   └── options.py
│
├── .gitignore
├── address_book.py
├── bot.py
├── completer.py
├── hints_collection.py
├── pyproject.toml
├── record.py
├── requirements-dev.txt
├── requirements.txt
└── README.md
```

We separated the handlers and utilities into folders to keep the project easier to navigate and avoid one huge `bot.py` 😅

---

## 🚀 How to Run

### First-time setup

Prerequisite: Python 3.9 or newer must be installed on your computer.

Use a separate virtual environment for this project. It keeps its tools and
dependencies isolated from other Python projects on your computer.

1. Clone the repository and open the project folder.

2. Create the virtual environment (only once per clone):

   macOS / Linux:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```powershell
   py -m venv .venv
   ```

3. Activate it before working on the project:

   macOS / Linux:

   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   Windows Command Prompt:

   ```bat
   .venv\Scripts\activate.bat
   ```

   Your terminal prompt should now start with `(.venv)`.

   If PowerShell blocks the activation script, run the following command for
   the current terminal, then activate the environment again:

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   ```

4. Install the project dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

   If you will change the code, install the development dependencies instead.
   This also installs all dependencies from `requirements.txt`:

   ```bash
   python -m pip install -r requirements-dev.txt
   ```

   In VS Code, select the virtual-environment interpreter through **Python:
   Select Interpreter**: `.venv/bin/python` on macOS/Linux or
   `.venv\Scripts\python.exe` on Windows.

5. If you use VS Code, install the official **Ruff** extension
   (`charliermarsh.ruff`). VS Code will also recommend it automatically when
   you open this project. The workspace settings format Python files, apply
   safe Ruff fixes, and organize imports when you save.

The `.venv/` folder is intentionally ignored by Git. Every developer creates
their own local environment; do not commit it.

### Start the bot

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

## ⌨️ Command suggestions

While entering a command or option, press `Tab` to search for values that
start with the text before the cursor. The result depends on the number of
matches:

- If there are no matches, the input remains unchanged.
- If there is one match, the bot completes the current command or option.
- If there are multiple matches, the bot displays them without changing the
  input.

The closest exact match is shown first, and the remaining matches are sorted
alphabetically.

For example, enter `add` and press `Tab`:

```text
Enter a command >>> add
Potential commands: add, add_address, add_birthday, add_contact, add_email, add_note
Enter a command >>> add
```

When only one command matches, `Tab` inserts it directly into the prompt:

```text
Before Tab: Enter a command >>> hell
After Tab:  Enter a command >>> hello
```

Autocomplete only changes the current input: it does not execute the command.
Pressing `Tab` on an empty prompt displays all available commands. Once you
start entering command arguments, `Tab` does not suggest argument values.

The exception is command options: after entering `-` as the first argument of
a valid command, press `Tab` to show matching options. Currently, the bot
supports the `--help` option. Because it is currently the only matching
option, `Tab` completes it directly:

```text
Before Tab: Enter a command >>> add --h
After Tab:  Enter a command >>> add --help
```

If more options are added later and several of them match the entered prefix,
the bot will display them as `Potential options` instead of completing the
input.

If you submit an incomplete command with `Enter`, the bot also displays
matching commands as a fallback:

```text
Enter a command >>> pho
Possible commands: phone
```

You must then enter the complete command yourself.

---

## 💡 Help

Add `--help` after any command to display its description, syntax, and an
example without executing the command:

```text
Enter a command >>> add --help
```

Use `help` to display all available command instructions. Commands with
aliases list every supported name in the same help entry, for example `add`
and `add_contact`.

---

## 🧹 Code style and linting

The project uses [Ruff](https://docs.astral.sh/ruff/) to check PEP 8 style
rules, import order, and common Python errors. GitHub Actions runs the same
lint check and verifies formatting for every push and pull request.

After activating `.venv`, install the development tools once:

```bash
python -m pip install -r requirements-dev.txt
```

Check the project locally:

```bash
python -m ruff check .
```

To apply safe automatic fixes, use:

```bash
python -m ruff check . --fix
```

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
| `help`  | Show instructions for all commands |
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

**Python** • **prompt_toolkit** • **OOP** • **Decorators** • **Regex** • **Datetime** • **Pickle** • **Git & GitHub**

Made as a team project while learning Python, working with Git, fixing bugs, and occasionally creating new ones in the process 😅
