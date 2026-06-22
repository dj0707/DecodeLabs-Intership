import getpass
import string
from dataclasses import dataclass


@dataclass
class PasswordReport:
    strength: str
    score: int
    checks: dict[str, bool]
    suggestions: list[str]


COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
    "letmein",
    "welcome123",
}


def analyse_password(password: str) -> PasswordReport:
    """Analyse a password and return its strength report."""
    checks = {
        "At least 8 characters": len(password) >= 8,
        "At least 12 characters": len(password) >= 12,
        "Contains uppercase letter": any(char.isupper() for char in password),
        "Contains lowercase letter": any(char.islower() for char in password),
        "Contains number": any(char.isdigit() for char in password),
        "Contains symbol": any(char in string.punctuation for char in password),
        "Not a common password": password.lower() not in COMMON_PASSWORDS,
        "No spaces": " " not in password,
    }

    # Main score uses the five core requirements from the project.
    core_score = sum(
        [
            checks["At least 8 characters"],
            checks["Contains uppercase letter"],
            checks["Contains lowercase letter"],
            checks["Contains number"],
            checks["Contains symbol"],
        ]
    )

    if not checks["At least 8 characters"] or not checks["Not a common password"]:
        strength = "Weak"
    elif core_score == 5 and checks["At least 12 characters"] and checks["No spaces"]:
        strength = "Strong"
    elif core_score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    suggestions = []

    if not checks["At least 8 characters"]:
        suggestions.append("Use at least 8 characters.")
    elif not checks["At least 12 characters"]:
        suggestions.append("Use 12 or more characters for stronger security.")

    if not checks["Contains uppercase letter"]:
        suggestions.append("Add at least one uppercase letter.")
    if not checks["Contains lowercase letter"]:
        suggestions.append("Add at least one lowercase letter.")
    if not checks["Contains number"]:
        suggestions.append("Add at least one number.")
    if not checks["Contains symbol"]:
        suggestions.append("Add at least one symbol such as !, @, #, or $.")
    if not checks["Not a common password"]:
        suggestions.append("Avoid common or leaked-style passwords.")
    if not checks["No spaces"]:
        suggestions.append("Remove spaces from the password.")

    if not suggestions:
        suggestions.append("The password satisfies all configured checks.")

    return PasswordReport(
        strength=strength,
        score=core_score,
        checks=checks,
        suggestions=suggestions,
    )


def display_report(report: PasswordReport) -> None:
    """Display the password analysis clearly."""
    print("\n" + "=" * 58)
    print("PASSWORD SECURITY REPORT")
    print("=" * 58)

    for requirement, passed in report.checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {requirement}")

    print("-" * 58)
    print(f"Core score : {report.score}/5")
    print(f"Strength   : {report.strength}")

    print("\nSuggestions:")
    for suggestion in report.suggestions:
        print(f"- {suggestion}")

    print("=" * 58)


def main() -> None:
    print("=" * 58)
    print("            PASSWORD STRENGTH CHECKER")
    print("=" * 58)
    print("The entered password is hidden while typing.")

    while True:
        password = getpass.getpass("\nEnter a password to test: ")
        report = analyse_password(password)
        display_report(report)

        again = input("\nCheck another password? (y/n): ").strip().lower()
        if again != "y":
            print("Program closed.")
            break


if __name__ == "__main__":
    main()
