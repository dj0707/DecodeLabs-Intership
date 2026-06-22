from caesar_cipher import caesar_encrypt, caesar_decrypt


def run_tests() -> None:
    test_cases = [
        ("ABC", 3, "DEF"),
        ("XYZ", 3, "ABC"),
        ("Hello, World!", 3, "Khoor, Zruog!"),
        ("Python 3.12", 5, "Udymts 3.12"),
    ]

    for plaintext, shift, expected in test_cases:
        encrypted = caesar_encrypt(plaintext, shift)
        decrypted = caesar_decrypt(encrypted, shift)

        assert encrypted == expected
        assert decrypted == plaintext

    print("All Project 2 tests passed successfully.")


if __name__ == "__main__":
    run_tests()
