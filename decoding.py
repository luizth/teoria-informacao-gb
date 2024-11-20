# decoding.py
from error_handling import InputError

def decode_codewords(codewords, method):
    if method == 1:
        return decode_repetition(codewords)
    elif method == 2:
        return decode_hamming(codewords)
    else:
        raise InputError("Invalid decoding method. Choose 1 for Repetition or 2 for Hamming.")

def decode_repetition(codewords, repeat_count=3):
    decoded = ""
    for i in range(0, len(codewords), repeat_count):
        bit_group = codewords[i:i+repeat_count]
        if len(bit_group) != repeat_count:
            raise InputError("Invalid codeword length for Repetition decoding.")

        # Majority voting
        bit_value = '1' if bit_group.count('1') > bit_group.count('0') else '0'
        decoded += bit_value
    return decoded

def decode_hamming(codewords):
    if len(codewords) % 7 != 0:
        raise InputError("Hamming (7,4) decoding requires codewords to be in 7-bit blocks.")

    decoded = ""
    for i in range(0, len(codewords), 7):
        codeword = codewords[i:i+7]
        decoded += hamming_7_4_decode(codeword)

    return decoded

def hamming_7_4_decode(codeword):
    if len(codeword) != 7:
        raise InputError("Hamming (7,4) decoding requires exactly 7 bits.")

    # Extract bits
    # p1, p2, d1, p3, d2, d3, d4 = map(int, codeword)  # Wikipedia uses this convention
    d1, d2, d3, d4, p1, p2, p3 = map(int, codeword)

    # Calculate syndrome
    s1 = p1 ^ d1 ^ d3 ^ d2  # d1 ^ d2 ^ d4
    s2 = p2 ^ d2 ^ d3 ^ d4  # d1 ^ d3 ^ d4
    s3 = p3 ^ d1 ^ d3 ^ d4  # d2 ^ d3 ^ d4
    syndrome = (s1 << 2) | (s2 << 1) | s3

    # Correct the error if syndrome is non-zero
    if syndrome != 0:
        corrected_codeword = list(codeword)
        error_position = syndrome - 1
        corrected_codeword[error_position] = '1' if corrected_codeword[error_position] == '0' else '0'
        codeword = ''.join(corrected_codeword)

    # Extract data bits
    # return f"{codeword[2]}{codeword[4]}{codeword[5]}{codeword[6]}"  # Wikipedia uses this convention
    return codeword[:4]

