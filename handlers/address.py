from utils.decorators import input_error_handler
from utils.helpers import check_for_arguments, check_if_record_exists


@input_error_handler
def add_address(book, *args):
    check_for_arguments(args, 2, ["name", "address"])

    name, *_ = args
    address = " ".join(args[1:])
    record = book.find(name)

    check_if_record_exists(record, name)

    record.add_address(address)
    print(f"Adding an address: {name} {address}")


@input_error_handler
def edit_address(book, *args):
    check_for_arguments(args, 2, ["name", "new_address"])

    name, *_ = args
    new_address = " ".join(args[1:])
    record = book.find(name)

    check_if_record_exists(record, name)

    old_address = record.get_address()
    record.edit_address(new_address)
    print(f"Editing address: {name}: {old_address} -> {new_address}")


@input_error_handler
def get_address(book, *args):
    check_for_arguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    check_if_record_exists(record, name)

    address = record.get_address()
    print(f"Address for {name}: {address}")


@input_error_handler
def remove_address(book, *args):
    check_for_arguments(args, 1, ["name"])

    name, *_ = args
    record = book.find(name)

    check_if_record_exists(record, name)

    record.remove_address()
    print(f"Address removed for {name}.")


command_handler_map = {
    "add_address": add_address,
    "edit_address": edit_address,
    "get_address": get_address,
    "remove_address": remove_address,
}
