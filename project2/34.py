34
class MyCustomException(Exception):
    """Exception raised for custom errors."""

    def __init__(self, message="This is a custom exception."):
        self.message = message
        super().__init__(self.message)


def check_input(value):
    """Check if input is valid and raise custom exception if not."""
    if not isinstance(value, int):
        raise MyCustomException("Input must be an integer.")


try:
    user_input = input("Enter an integer: ")
    check_input(user_input)
    print("Input is valid.")
except MyCustomException as e:
    print("Error:", e)
