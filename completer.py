from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings


def find_command(command: str, all_commands: list[str]) -> list[str]:
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
    all_options: list[str],
) -> tuple[str, list[str]]:
    normalized_text = text_before_cursor.lower()

    if not normalized_text.strip():
        return "commands", all_commands

    if normalized_text[-1].isspace():
        return "", []

    tokens = normalized_text.split()

    if len(tokens) == 1:
        return "commands", find_command(tokens[0], all_commands)

    if len(tokens) == 2:
        command, option_prefix = tokens

        if command in all_commands and option_prefix.startswith("-"):
            return "options", find_command(option_prefix, all_options)

    return "", []


def create_autocomplete_bindings(
    all_commands: list[str],
    all_options: list[str],
) -> KeyBindings:
    bindings = KeyBindings()

    @bindings.add("tab")
    async def handle_tab(event) -> None:
        text_before_cursor = event.current_buffer.document.text_before_cursor

        suggestion_type, suggestions = get_tab_suggestions(
            text_before_cursor,
            all_commands,
            all_options,
        )

        if not suggestions:
            return

        message = f"Potential {suggestion_type}: {', '.join(suggestions)}"

        await run_in_terminal(lambda: print(message))

    return bindings
