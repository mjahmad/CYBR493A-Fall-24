# Simple Caesar Cipher and Character Swapping Encryption/Decryption
# Full documentation provided for each function

# Simple Caesar Cipher

def caesar_cipher_simple_encrypt(message, shift):
    """
    Encrypts a message using a simple Caesar Cipher.

    Args:
        message (str): The message to be encrypted.
        shift (int): The number of positions each character is shifted in the alphabet.

    Returns:
        str: The encrypted message where each letter is shifted by the 'shift' value.

    Example:
        caesar_cipher_simple_encrypt("abc", 2) -> "cde"
    """
    encrypted_message = ""  # Initialize an empty string to store the encrypted message

    # Loop through each character in the message
    for char in message:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Shift the character's ASCII value by 'shift' and convert it back to a character
            shifted_char = chr(ord(char) + shift)
            encrypted_message += shifted_char  # Append the shifted character to the encrypted message
        else:
            # If the character is not a letter (e.g., punctuation or space), keep it unchanged
            encrypted_message += char

    return encrypted_message  # Return the final encrypted message


def caesar_cipher_simple_decrypt(encrypted_message, shift):
    """
    Decrypts a message that was encrypted using a simple Caesar Cipher.

    Args:
        encrypted_message (str): The encrypted message.
        shift (int): The number of positions each character was shifted in the alphabet during encryption.

    Returns:
        str: The decrypted message where each letter is shifted back by the 'shift' value.

    Example:
        caesar_cipher_simple_decrypt("cde", 2) -> "abc"
    """
    decrypted_message = ""  # Initialize an empty string to store the decrypted message

    # Loop through each character in the encrypted message
    for char in encrypted_message:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Reverse the shift applied during encryption by subtracting 'shift' from the ASCII value
            shifted_char = chr(ord(char) - shift)
            decrypted_message += shifted_char  # Append the shifted character to the decrypted message
        else:
            # If the character is not a letter, keep it unchanged
            decrypted_message += char

    return decrypted_message  # Return the final decrypted message


# Simple Character Swapping (ASCII shift by 1)

def swap_cipher_encrypt(message):
    """
    Encrypts a message by shifting each character's ASCII value by 1.

    Args:
        message (str): The message to be encrypted.

    Returns:
        str: The encrypted message where each character is replaced by its next ASCII character.

    Example:
        swap_cipher_encrypt("abc") -> "bcd"
    """
    encrypted_message = ""  # Initialize an empty string to store the encrypted message

    # Loop through each character in the message
    for char in message:
        # Shift the character's ASCII value by 1 and convert it back to a character
        encrypted_message += chr(ord(char) + 1)

    return encrypted_message  # Return the final encrypted message


def swap_cipher_decrypt(encrypted_message):
    """
    Decrypts a message that was encrypted using simple character swapping (ASCII shift by 1).

    Args:
        encrypted_message (str): The encrypted message.

    Returns:
        str: The decrypted message where each character is replaced by its previous ASCII character.

    Example:
        swap_cipher_decrypt("bcd") -> "abc"
    """
    decrypted_message = ""  # Initialize an empty string to store the decrypted message

    # Loop through each character in the encrypted message
    for char in encrypted_message:
        # Reverse the ASCII shift by 1 to get the original character
        decrypted_message += chr(ord(char) - 1)

    return decrypted_message  # Return the final decrypted message


# Example Usage
message = "Hello World!"  # Define a sample message

# Simple Caesar Cipher with a shift of 2
shift = 2  # Set the shift value for the Caesar Cipher

# Encrypt and decrypt using Caesar Cipher
encrypted_caesar_simple = caesar_cipher_simple_encrypt(message, shift)  # Encrypt the message
decrypted_caesar_simple = caesar_cipher_simple_decrypt(encrypted_caesar_simple, shift)  # Decrypt the message

# Display the results for the Caesar Cipher
print("Original Message:", message)
print("Caesar Cipher Encrypted (Simple):", encrypted_caesar_simple)
print("Caesar Cipher Decrypted (Simple):", decrypted_caesar_simple)

# Simple Character Swapping
# Encrypt and decrypt using character swapping
encrypted_swap = swap_cipher_encrypt(message)  # Encrypt the message
decrypted_swap = swap_cipher_decrypt(encrypted_swap)  # Decrypt the message

# Display the results for the character swapping cipher
print("\nSwap Cipher Encrypted:", encrypted_swap)
print("Swap Cipher Decrypted:", decrypted_swap)
