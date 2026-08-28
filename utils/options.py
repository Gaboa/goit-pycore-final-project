def get_help_hint(command, hints_list):
    instruction = hints_list[command]

    if instruction:
        return instruction

    return "--help is not available for '{command}' yet"


def get_all_help_hints(hints_list):
    return "\n\n".join(dict.fromkeys(hints_list.values()))
