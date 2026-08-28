from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings


def find_command(command: str, all_commands: list[str]):
    potential_commands = [
        valid_command
        for valid_command in all_commands
        if valid_command.startswith(command)
    ]

    return sorted(
        potential_commands,
        key=lambda valid_command: (
            valid_command != command,
            valid_command,
        ),
    )


def get_tab_suggestions(
    text_before_cursor: str,
    all_commands: list[str],
) -> list[str]:
    normalize_text = text_before_cursor.lower()

    if not normalize_text.strip():
        return all_commands

    if len(normalize_text.split(" ")) >= 1 and normalize_text[-1] == " ":
        return []

    return find_command(normalize_text, all_commands)


def create_autocomplete_bindings(
    all_commands: list[str],
) -> KeyBindings:
    bindings = KeyBindings()

    @bindings.add("tab")
    async def handle_tab(event):
        text_before_cursor = event.current_buffer.document.text_before_cursor

        suggestions = get_tab_suggestions(
            text_before_cursor,
            all_commands,
        )

        if not suggestions:
            return

        message = f"Potential commands: {', '.join(suggestions)}"

        await run_in_terminal(lambda: print(message))

    return bindings
