# encoding.py
from error_handling import InputError

def encode_symbols(symbols, method):
    if method == 1:
        return encode_repetition(symbols)
    elif method == 2:
        return encode_hamming(symbols)
    else:
        raise InputError("Invalid encoding method. Choose 1 for Repetition or 2 for Hamming.")

def encode_repetition(symbols, repeat_count=3):
    return ''.join(bit * repeat_count for bit in symbols)

def encode_hamming(symbols):
    if len(symbols) % 4 != 0:
        raise InputError("Hamming (7,4) encoding requires symbols to be in 4-bit blocks.")

    encoded = ""
    for i in range(0, len(symbols), 4):
        data_bits = symbols[i:i+4]
        encoded += hamming_7_4_encode(data_bits)

    return encoded

def hamming_7_4_encode(data_bits):
    d1, d2, d3, d4 = map(int, data_bits)

    # Calculate parity bits
    p1 = d1 ^ d3 ^ d2
    p2 = d2 ^ d3 ^ d4
    p3 = d1 ^ d3 ^ d4

    return f"{d1}{d2}{d3}{d4}{p1}{p2}{p3}"
