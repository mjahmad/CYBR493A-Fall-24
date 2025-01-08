"""
Character Shift with ASCII Range Wrapping:
Shift all characters (letters, numbers, and special characters) by a fixed value.
Wrap around if the shifted character goes beyond the ASCII range of printable characters (from 32 to 126 in ASCII).
Number Substitution:
Replace digits (0-9) with a different fixed digit. For example, 0 -> 9, 1 -> 8, etc.

"""


# Creative Encryption: Character Shift and Number Substitution

def shift_characters(message, shift):
    """
    Encrypts the message by shifting characters by a fixed value with ASCII wrapping.

    Args:
        message (str): The original message to be encrypted.
        shift (int): The shift value to apply to each character.

    Returns:
        str: The encrypted message where characters are shifted with ASCII wrapping.

    Example:
        shift_characters("Hello!", 5) -> "Mjqqt%"
    """
    encrypted_message = ""

    for char in message:
        # Convert the character to its ASCII value, shift it, and wrap if needed
        ascii_val = ord(char)
        shifted_val = ascii_val + shift

        # ASCII range for printable characters is 32-126. If it goes beyond, wrap around.
        if shifted_val > 126:
            shifted_val = 32 + (shifted_val - 127)
        elif shifted_val < 32:
            shifted_val = 126 - (31 - shifted_val)

        # Convert back to character and append to encrypted message
        encrypted_message += chr(shifted_val)

    return encrypted_message


def substitute_numbers(message):
    """
    Substitutes numbers with fixed alternate numbers.
    0 -> 9, 1 -> 8, 2 -> 7, ..., 9 -> 0.

    Args:
        message (str): The message containing numbers.

    Returns:
        str: The message with substituted numbers.

    Example:
        substitute_numbers("123") -> "876"
    """
    # Define a dictionary for number substitution
    num_substitution = {'0': '9', '1': '8', '2': '7', '3': '6', '4': '5',
                        '5': '4', '6': '3', '7': '2', '8': '1', '9': '0'}

    encrypted_message = ""

    for char in message:
        # If the character is a number, substitute it
        if char in num_substitution:
            encrypted_message += num_substitution[char]
        else:
            encrypted_message += char  # Leave other characters unchanged

    return encrypted_message


def encrypt_message(message, shift):
    """
    Encrypts the message by first shifting characters and then substituting numbers.

    Args:
        message (str): The original message to be encrypted.
        shift (int): The shift value for character encryption.

    Returns:
        str: The fully encrypted message.

    Example:
        encrypt_message("Hello 123!", 3) -> "Khoor 876$"
    """
    # Step 1: Shift characters using the shift_characters function
    shifted_message = shift_characters(message, shift)

    # Step 2: Substitute numbers using the substitute_numbers function
    encrypted_message = substitute_numbers(shifted_message)

    return encrypted_message


def decrypt_message(encrypted_message, shift):
    """
    Decrypts the message by first reversing the number substitution and then reversing the character shift.

    Args:
        encrypted_message (str): The encrypted message to be decrypted.
        shift (int): The shift value used in encryption.

    Returns:
        str: The decrypted original message.

    Example:
        decrypt_message("Khoor 876$", 3) -> "Hello 123!"
    """
    # Step 1: Reverse the number substitution by reusing substitute_numbers
    decrypted_message = substitute_numbers(encrypted_message)

    # Step 2: Reverse the character shift by applying negative shift
    original_message = shift_characters(decrypted_message, -shift)

    return original_message


# Example Usage
message = "Hello World! 123"
shift_value = 5  # Shift value for the encryption

# Encrypt the message
encrypted = encrypt_message(message, shift_value)
# Decrypt the message back to the original
decrypted = decrypt_message(encrypted, shift_value)

# Output the results
print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
