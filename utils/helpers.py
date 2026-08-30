def check_if_record_exists(record, name):
    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")


def check_for_arguments(args, length: int, names: list[str]):
    if len(args) < length:
        raise ValueError(
            "Insufficient arguments for this command. Please provide the "
            f"following arguments: {', '.join(names)}."
        )


def check_empty_phone_number(args):
    if len(args) == 1:
        raise ValueError("Phone number cannot be empty.")
