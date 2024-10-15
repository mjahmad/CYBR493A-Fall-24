# Caesar Cipher Brute-Force Attack using Python
# Usage: python caesar_brute_force.py "<ciphertext>"

import sys


def caesar_decrypt(ciphertext, shift):
    """Decrypts the Caesar cipher by shifting each letter by the given shift."""
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            # Normalize to lowercase and perform the shift
            shifted = ord(char.lower()) - shift
            # Wrap around if needed
            if shifted < ord('a'):
                shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char  # Non-alphabetical characters remain unchanged
    return decrypted


def brute_force_caesar(ciphertext):
    """Tries all 26 possible shifts to decrypt the Caesar cipher."""
    print("Brute-force results for Caesar Cipher:\n")
    for shift in range(1, 27):
        print(f"Shift {shift}: {caesar_decrypt(ciphertext, shift)}\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python caesar_brute_force.py '<ciphertext>'")
        sys.exit(1)

    # Get the ciphertext from the command line argument
    ciphertext = sys.argv[1]

    # Perform brute-force decryption
    brute_force_caesar(ciphertext)
