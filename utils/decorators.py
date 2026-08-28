def input_error_handler(func):
    def wrapper(book, *args):
        try:
            return func(book, *args)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return wrapper
