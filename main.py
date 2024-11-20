# main.py
from input_validation import validate_symbols, validate_codewords
from error_handling import InputError
from encoding import encode_symbols
from decoding import decode_codewords


def main():
    print("Welcome to the Error Detection and Correction CLI")
    print("Choose an operation:")
    print("1. Encode Symbols")
    print("2. Decode Codewords")

    try:
        choice = int(input("Enter your choice (1 or 2): ").strip())
        if choice not in [1, 2]:
            raise InputError("Invalid choice. Please enter 1 or 2.")

        # Get symbols or codewords
        if choice == 1:
            symbols = input("Enter symbols to encode (binary): ").strip()
            validate_symbols(symbols)
            print("Choose encoding method:")
            print("1. Repetition Code (Ri)")
            print("2. Hamming (7,4)")
            method = int(input("Enter your choice (1 or 2): ").strip())
            encoded_result = encode_symbols(symbols, method)
            print(f"Encoded Result: {encoded_result}")

        elif choice == 2:
            codewords = input("Enter codewords to decode (binary): ").strip()
            validate_codewords(codewords)
            print("Choose decoding method:")
            print("1. Repetition Code (Ri)")
            print("2. Hamming (7,4)")
            method = int(input("Enter your choice (1 or 2): ").strip())
            decoded_result = decode_codewords(codewords, method)
            print(f"Decoded Result: {decoded_result}")

    except InputError as e:
        print(f"Input Error: {e}")
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
