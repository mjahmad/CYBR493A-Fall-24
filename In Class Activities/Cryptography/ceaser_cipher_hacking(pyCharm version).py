# Caesar Cipher Brute-Force Attack using Python (PyCharm compatible)
# This version allows input from the user via the console

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
    # Ask the user for the ciphertext input
    ciphertext = input("Enter the ciphertext to decrypt: ")

    # Perform brute-force decryption
    brute_force_caesar(ciphertext)
