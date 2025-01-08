# Creative Encryption and Decryption: Word Reversal with Vowel Shifting

def reverse_words(message):
    """
    Reverses each word in the sentence while keeping the word order intact.

    Args:
        message (str): The message to be encrypted.

    Returns:
        str: The message with each word reversed.

    Example:
        reverse_words("Hello World") -> "olleH dlroW"
    """
    # Split the message into words, reverse each word, then join them back into a sentence
    reversed_message = ' '.join(word[::-1] for word in message.split())
    return reversed_message


def shift_vowels(message):
    """
    Shifts vowels (a, e, i, o, u) to the next vowel in the sequence.
    'a' -> 'e', 'e' -> 'i', 'i' -> 'o', 'o' -> 'u', 'u' -> 'a'

    Args:
        message (str): The message to be encrypted.

    Returns:
        str: The message with shifted vowels.

    Example:
        shift_vowels("hello") -> "hillu"
    """
    vowel_shift = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
                   'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}

    shifted_message = ""
    for char in message:
        # If the character is a vowel, replace it with the next vowel in the sequence
        if char in vowel_shift:
            shifted_message += vowel_shift[char]
        else:
            shifted_message += char  # If not a vowel, keep the character as is

    return shifted_message


def encrypt_message(message):
    """
    Encrypts a message by reversing each word and shifting the vowels.

    Args:
        message (str): The original message to be encrypted.

    Returns:
        str: The encrypted message.

    Example:
        encrypt_message("Hello World") -> "illuH dlrU"
    """
    # Step 1: Reverse each word in the message
    reversed_message = reverse_words(message)

    # Step 2: Shift the vowels in the reversed message
    encrypted_message = shift_vowels(reversed_message)

    return encrypted_message


def decrypt_message(encrypted_message):
    """
    Decrypts a message that was encrypted using word reversal and vowel shifting.

    Args:
        encrypted_message (str): The encrypted message to be decrypted.

    Returns:
        str: The decrypted original message.

    Example:
        decrypt_message("illuH dlrU") -> "Hello World"
    """
    # Step 1: Reverse the vowel shifting
    # Inverse vowel shift (opposite of the encryption shift)
    inverse_vowel_shift = {'e': 'a', 'i': 'e', 'o': 'i', 'u': 'o', 'a': 'u',
                           'E': 'A', 'I': 'E', 'O': 'I', 'U': 'O', 'A': 'U'}

    decrypted_message = ""
    for char in encrypted_message:
        if char in inverse_vowel_shift:
            decrypted_message += inverse_vowel_shift[char]
        else:
            decrypted_message += char  # Keep non-vowel characters the same

    # Step 2: Reverse the words back to their original form
    original_message = reverse_words(decrypted_message)

    return original_message


# Example Usage
message = "Hello World from - This is craetive, but not critical really !"

# Encrypt the message
encrypted = encrypt_message(message)
# Decrypt the message back to the original
decrypted = decrypt_message(encrypted)

# Output
print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
