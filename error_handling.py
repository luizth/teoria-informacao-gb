# error_handling.py

class InputError(Exception):
    """Exception raised for errors in the input."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)
