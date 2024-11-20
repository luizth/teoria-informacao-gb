# test_decoding.py
import unittest
from decoding import decode_codewords, decode_repetition, decode_hamming
from error_handling import InputError

class TestDecoding(unittest.TestCase):

    def test_decode_repetition(self):
        # Standard test with repeat count = 3
        self.assertEqual(decode_repetition("111000111"), "101")

        # Different repeat count (2)
        self.assertEqual(decode_repetition("110011", repeat_count=2), "101")

        # Edge case: Codeword length not divisible by repeat count (should raise InputError)
        with self.assertRaises(InputError):
            decode_repetition("11100")

    def test_decode_hamming(self):
        # Standard 7-bit Hamming codeword
        self.assertEqual(decode_hamming("1000101"), "1000")

        # Correctable single-bit error
        self.assertEqual(decode_hamming("1010010"), "1010")  # Error in first bit

        # Edge case: Invalid codeword length (not 7 bits)
        with self.assertRaises(InputError):
            decode_hamming("1111")

    def test_decode_codewords_repetition(self):
        # Test main function for Repetition Code decoding
        self.assertEqual(decode_codewords("111000111", method=1), "101")

    def test_decode_codewords_hamming(self):
        # Test main function for Hamming (7,4) decoding
        self.assertEqual(decode_codewords("1011001", method=2), "1011")

    def test_decode_codewords_invalid_method(self):
        # Test invalid decoding method (should raise an InputError)
        with self.assertRaises(InputError):
            decode_codewords("111000", method=3)

if __name__ == '__main__':
    unittest.main()
