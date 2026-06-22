"""
Cyber Security Project 2
Basic Encryption and Decryption using the Caesar Cipher
"""


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text using a Caesar cipher."""
    encrypted_text = ""
    shift %= 26

    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.islower():
            encrypted_text += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            encrypted_text += char

    return encrypted_text


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt Caesar-cipher text using the same shift key."""
    return caesar_encrypt(text, -shift)


def read_shift_key() -> int:
    while True:
        try:
            return int(input("Enter shift key: "))
        except ValueError:
            print("Please enter a whole number.")


def main() -> None:
    print("=" * 55)
    print("     BASIC ENCRYPTION AND DECRYPTION SYSTEM")
    print("=" * 55)

    while True:
        print("\n1. Encrypt text")
        print("2. Decrypt text")
        print("3. Encrypt and verify")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            text = input("Enter plaintext: ")
            shift = read_shift_key()
            print("Encrypted text:", caesar_encrypt(text, shift))

        elif choice == "2":
            text = input("Enter ciphertext: ")
            shift = read_shift_key()
            print("Decrypted text:", caesar_decrypt(text, shift))

        elif choice == "3":
            text = input("Enter plaintext: ")
            shift = read_shift_key()
            encrypted = caesar_encrypt(text, shift)
            decrypted = caesar_decrypt(encrypted, shift)

            print("Original text :", text)
            print("Encrypted text:", encrypted)
            print("Decrypted text:", decrypted)
            print("Verification  :", "SUCCESS" if decrypted == text else "FAILED")

        elif choice == "4":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
