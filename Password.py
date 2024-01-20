import string
import random
import argparse

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type (letters, numbers, symbols) must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate random passwords.")
    parser.add_argument("length", type=int, help="Length of the password")
    parser.add_argument("--letters", action="store_true", help="Include letters in the password")
    parser.add_argument("--numbers", action="store_true", help="Include numbers in the password")
    parser.add_argument("--symbols", action="store_true", help="Include symbols in the password")

    args = parser.parse_args()

    password = generate_password(args.length, args.letters, args.numbers, args.symbols)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
