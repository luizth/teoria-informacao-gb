# utils.py

def binary_to_integer(binary_str):
    """Convert a binary string to an integer."""
    return int(binary_str, 2)

def integer_to_binary(integer, length=7):
    """Convert an integer to a binary string of a fixed length (default 7 bits)."""
    return format(integer, f'0{length}b')
