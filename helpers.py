def checkIfRecordExists(record, name):
    if record is None:
        raise ValueError(f"Contact with name '{name}' does not exist.")

def checkForArguments(args, length: int, names: list[str]):
    if len(args) < length:
        raise ValueError(f"Insufficient arguments for this command. Please provide the following arguments: {', '.join(names)}.")