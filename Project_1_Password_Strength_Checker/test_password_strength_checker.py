from password_strength_checker import analyse_password


def run_tests() -> None:
    cases = [
        ("abc", "Weak"),
        ("Password1", "Medium"),
        ("Password1!", "Medium"),
        ("SecurePass123!", "Strong"),
        ("password123", "Weak"),
    ]

    for password, expected_strength in cases:
        result = analyse_password(password)
        assert result.strength == expected_strength, (
            f"{password!r}: expected {expected_strength}, "
            f"got {result.strength}"
        )

    print("All Project 1 tests passed successfully.")


if __name__ == "__main__":
    run_tests()
