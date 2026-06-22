# Project 2: Basic Encryption and Decryption

## Goal
Encrypt and decrypt user text using a Caesar cipher.

## Requirements implemented
- User text input
- User-selected shift key
- Encryption
- Decryption
- Encrypted and decrypted output
- Uppercase and lowercase support
- Spaces, numbers, and punctuation preserved
- Automatic verification

## Run

```bash
python caesar_cipher.py
```

## Test

```bash
python test_caesar_cipher.py
```

## Formula

```text
Encryption: E(x) = (x + n) mod 26
Decryption: D(x) = (x - n) mod 26
```

## Security note
The Caesar cipher is educational and should not be used to protect real sensitive data.
