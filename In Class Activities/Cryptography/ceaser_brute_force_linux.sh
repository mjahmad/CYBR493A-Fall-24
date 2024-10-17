#!/bin/bash

# Caesar Cipher Brute-Force Attack using Bash
# Usage: ./caesar_brute_force.sh "<ciphertext>"

# Input: Ciphertext provided as the first argument
ciphertext=$1

# The alphabet (lowercase only)
alphabet="abcdefghijklmnopqrstuvwxyz"

# Convert the ciphertext to lowercase for simplicity
ciphertext=$(echo "$ciphertext" | tr 'A-Z' 'a-z')

# Function to shift the letters by 'n' positions
shift_cipher() {
    shift=$1
    echo "$ciphertext" | tr "${alphabet:0:26}" "${alphabet:$shift:26}${alphabet:0:$shift}"
}

# Brute-force loop through all 26 possible shifts
for shift in {1..26}; do
    echo "Shift $shift:"
    shift_cipher $shift
    echo
done
