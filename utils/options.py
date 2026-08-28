def get_help_hint(command, hints_list):
    instruction = hints_list[command]

    if instruction:
        return instruction

    return "--help is not available for '{command}' yet"
