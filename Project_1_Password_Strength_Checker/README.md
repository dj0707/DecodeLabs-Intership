# Project 1: Password Strength Checker

## Goal
Create a Python program that checks whether a password is weak, medium, or strong.

## PDF requirements implemented
- Checks password length
- Checks uppercase letters
- Checks lowercase letters
- Checks numbers
- Checks symbols
- Displays password strength
- Uses string handling and conditional logic
- Uses Python's `any()` for clear linear-time checks
- Adds suggestions for improving weak passwords
- Avoids printing the password on screen while typing

## Strength rules

### Weak
- Fewer than 8 characters, or
- A commonly used password, or
- Too few character categories

### Medium
- At least 8 characters
- Meets at least three core checks

### Strong
- At least 12 characters
- Includes uppercase, lowercase, number, and symbol
- Is not in the common-password list
- Contains no spaces

## Run

```bash
python password_strength_checker.py
```

On Windows, you may use:

```bash
py password_strength_checker.py
```

## Test

```bash
python test_password_strength_checker.py
```

## Example

Password:

```text
SecurePass123!
```

Result:

```text
Strength: Strong
Core score: 5/5
```

## Security note
This is an educational password evaluator. Real systems should also use secure password hashing, rate limiting, multi-factor authentication, and checks against known breached-password databases.
