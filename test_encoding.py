# test_encoding.py
import unittest
from encoding import encode_symbols, encode_repetition, encode_hamming
from error_handling import InputError

class TestEncoding(unittest.TestCase):

    def test_encode_repetition(self):
        # Basic test with repeat count = 3
        self.assertEqual(encode_repetition("101"), "111000111")

        # Different repeat count (2)
        self.assertEqual(encode_repetition("101", repeat_count=2), "110011")

        # Edge case: Empty input
        self.assertEqual(encode_repetition(""), "")

    def test_encode_hamming(self):
        # Standard 4-bit input for Hamming (7,4)
        self.assertEqual(encode_hamming("1000"), "1000101")
        self.assertEqual(encode_hamming("1010"), "1010010")

        # Edge case: Empty input
        self.assertEqual(encode_hamming(""), "")

        # Input not multiple of 4 (should raise)
        with self.assertRaises(InputError):
            encode_hamming("101")

    def test_encode_symbols_repetition(self):
        # Test main function for Repetition Code
        self.assertEqual(encode_symbols("101", method=1), "111000111")

    def test_encode_symbols_hamming(self):
        # Test main function for Hamming (7,4)
        self.assertEqual(encode_symbols("1011", method=2), "1011001")

    def test_encode_symbols_invalid_method(self):
        # Test invalid encoding method (should raise an InputError)
        with self.assertRaises(InputError):
            encode_symbols("101", method=3)

if __name__ == '__main__':
    unittest.main()
