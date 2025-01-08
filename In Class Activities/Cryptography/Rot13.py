#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Ed Goad
# date: 2/5/2021
"""
How it works See page 89 of the Python for Cybersecurity book.
The script starts on line #7 by prompting the user for a message to either encrypt or decrypt. This
message is then converted to lower-case on line #9 to simplify our script.
On line #13 we begin a for loop to break our message into individual letters. These letters will be
converted one at a time.
Chapter 5: Cryptography 89
On line #15 the letter is converted to the ASCII equivalent number using the ord() built-in Python
function. If we look at the ASCII table, this means the letter “a” will be converted to the number 97.
On line #17 the number is evaluated to see if it is between 97 and 122, the ASCII values for the letters
a and z respectively. If the number is out of that range, we can assume it isn’t a letter and instead
is punctuation such as :”,’#; or other similar characters that we will ignore. If that is the case, we
skip to line #26 where the ASCII value is converted back into the character and appended to the
final_message string.
If the ascii_num is found to contain a valid letter, on line #19 new_ascii is assigned ascii_num + 13
to “shift” it.
At this point it is possible we “shifted” the letter too far, beyond the letter z and into non-printable
characters. To resolve this, on line #21 we check the value of new_ascii to see if it has moved past
the letter z. If we find we have gone too far, we “wrap-around” to the beginning of the alphabet by
subtracting 26 from the value.
Lastly, the final_message is printed to the console for the user
"""
# Prompt for the source message
source_message = input("What is the message to encrypt/decrypt? ")
# Convert message to lower-case for simplicity
source_message = source_message.lower()
final_message = ""

# Loop through each letter in the source message
for letter in source_message:
    # Convert the letter to the ASCII equivalent
    ascii_num = ord(letter)
    # Check to see if an alphabetic (a-z) character, 
    # if not, skip
    if ascii_num >= 97 and ascii_num <= 122:
        # Add 13 to ascii_num to "shift" it by 13
        new_ascii = ascii_num + 13
        # Confirm new character will be alphabetic 
        if new_ascii > 122:
            # If not, wrap around
            new_ascii = new_ascii - 26
        final_message = final_message + chr(new_ascii)
    else:
        final_message = final_message + chr(ascii_num)

# Print converted message
print("Message has been converted:")
print(final_message)