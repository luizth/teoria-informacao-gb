# input_validation.py
from error_handling import InputError

def validate_symbols(symbols):
    if not symbols or not all(c in '01' for c in symbols):
        raise InputError("Symbols must be a non-empty binary string (e.g., '10101').")

def validate_codewords(codewords):
    if not codewords or not all(c in '01' for c in codewords):
        raise InputError("Codewords must be a non-empty binary string (e.g., '1100110').")
