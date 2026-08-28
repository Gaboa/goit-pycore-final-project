def get_help_hint(command: str, hints_list: dict[str, str]) -> str:
    instruction = hints_list[command]

    if instruction:
        return instruction

    return "--help is not available for '{command}' yet"


def get_all_help_hints(hints_list: dict[str, str]) -> str:
    return "\n\n".join(dict.fromkeys(hints_list.values()))
